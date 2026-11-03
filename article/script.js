const progress=document.querySelector('.progress');
function updateProgress(){const range=document.documentElement.scrollHeight-innerHeight;progress.style.width=(range>0?scrollY/range*100:0)+'%';}
addEventListener('scroll',updateProgress,{passive:true});addEventListener('resize',updateProgress);updateProgress();
const mobileContents=document.querySelector('.mobile-contents');
const mobileCurrent=document.querySelector('.mobile-current');
const links=[...document.querySelectorAll('.contents a,.mobile-contents nav a')];
function markSection(){let current=null;document.querySelectorAll('article>section').forEach(s=>{if(s.getBoundingClientRect().top<=innerHeight*.3)current=s.id;});links.forEach(link=>{const active=link.hash==='#'+current;link.classList.toggle('active',active);if(active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});const active=links.find(link=>link.hash==='#'+current);mobileCurrent.textContent=active?active.textContent:mobileCurrent.dataset.placeholder;}
addEventListener('scroll',markSection,{passive:true});addEventListener('resize',markSection);markSection();
document.querySelectorAll('a[href^="#"]:not([data-time])').forEach(link=>link.addEventListener('click',event=>{
  if(event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
  const target=document.getElementById(link.hash.slice(1));
  if(!target)return;
  event.preventDefault();mobileContents.open=false;
  if(location.hash!==link.hash)history.pushState(null,'',link.hash);
  preserveSection(link.hash);
  target.scrollIntoView({block:'start',behavior:'instant'});
  markSection();updateProgress();
}));
document.addEventListener('click',event=>{if(mobileContents.open&&!mobileContents.contains(event.target))mobileContents.open=false;});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&mobileContents.open){mobileContents.open=false;mobileContents.querySelector('summary').focus();}});
addEventListener('resize',()=>{if(!matchMedia('(max-width:740px)').matches)mobileContents.open=false;});
function preserveSection(fragment=location.hash){document.querySelectorAll('[data-language]').forEach(link=>{link.setAttribute('href',link.getAttribute('href').split('#')[0]+fragment);});}
addEventListener('hashchange',()=>preserveSection());preserveSection();
const dialog=document.querySelector('.lightbox');let opener;
if(typeof dialog.showModal==='function'){document.querySelectorAll('figure img').forEach(img=>{img.tabIndex=0;img.setAttribute('role','button');img.setAttribute('aria-label',document.body.dataset.enlarge+': '+img.alt);function open(){opener=img;dialog.querySelector('img').src=img.src;dialog.querySelector('img').alt=img.alt;dialog.querySelector('p').textContent=img.closest('figure').querySelector('figcaption').textContent;dialog.showModal();}img.addEventListener('click',open);img.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();open();}});});dialog.querySelector('.close').addEventListener('click',()=>dialog.close());dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});dialog.addEventListener('close',()=>opener?.focus());}
const video=document.querySelector('#main-film');
document.querySelectorAll('[data-time]').forEach(control=>control.addEventListener('click',event=>{
  event.preventDefault();
  const time=Number(control.dataset.time);
  document.querySelectorAll('video').forEach(clip=>{if(clip!==video)clip.pause();});
  function seek(){
    video.currentTime=time;
    history.replaceState(null,'','#film');preserveSection('#film');
    video.scrollIntoView({block:'center',behavior:'instant'});
    video.focus({preventScroll:true});
  }
  if(video.readyState>=1)seek();
  else{video.addEventListener('loadedmetadata',seek,{once:true});video.load();}
}));
