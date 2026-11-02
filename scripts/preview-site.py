"""Loopback-only preview with byte ranges, so HTML video seeking works locally."""
import argparse
import functools
import http.server
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Handler(http.server.SimpleHTTPRequestHandler):
    def handle(self):
        try:return super().handle()
        except (ConnectionResetError,BrokenPipeError):
            # Browsers cancel previous media requests when seeking or navigating.
            return None
    def send_head(self):
        self.byte_range=None
        value=self.headers.get('Range')
        path=Path(self.translate_path(self.path))
        if not value or not path.is_file():return super().send_head()
        match=re.fullmatch(r'bytes=(\d*)-(\d*)',value)
        size=path.stat().st_size
        if not match or not any(match.groups()):
            self.send_error(416,'Unsupported byte range');return None
        a,b=match.groups()
        start=int(a) if a else max(0,size-int(b))
        end=min(int(b),size-1) if a and b else size-1
        if start>end or start>=size:
            self.send_response(416);self.send_header('Content-Range',f'bytes */{size}');self.end_headers();return None
        f=path.open('rb');f.seek(start);self.byte_range=(start,end)
        self.send_response(206)
        self.send_header('Content-Type',self.guess_type(str(path)))
        self.send_header('Accept-Ranges','bytes')
        self.send_header('Content-Range',f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length',str(end-start+1))
        self.end_headers();return f
    def copyfile(self,source,outputfile):
        if self.byte_range is None:return super().copyfile(source,outputfile)
        remaining=self.byte_range[1]-self.byte_range[0]+1
        while remaining:
            data=source.read(min(65536,remaining))
            if not data:break
            outputfile.write(data);remaining-=len(data)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--port',type=int,default=8765);args=p.parse_args()
    directory=ROOT/'work/site-dist'
    if not (directory/'index.html').is_file():p.error('Run build-article.py and build-site.py first.')
    handler=functools.partial(Handler,directory=str(directory))
    server=http.server.ThreadingHTTPServer(('127.0.0.1',args.port),handler)
    print(f'Preview: http://127.0.0.1:{args.port}/',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
