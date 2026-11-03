const progress=document.querySelector('.progress');
function updateProgress(){const range=document.documentElement.scrollHeight-innerHeight;progress.style.width=(range>0?scrollY/range*100:0)+'%';}
addEventListener('scroll',updateProgress,{passive:true});addEventListener('resize',updateProgress);updateProgress();
const links=[...document.querySelectorAll('.contents a')];
function markSection(){let current=null;document.querySelectorAll('article>section').forEach(s=>{if(s.getBoundingClientRect().top<=innerHeight*.3)current=s.id;});links.forEach(link=>{const active=link.hash==='#'+current;link.classList.toggle('active',active);if(active)link.setAttribute('aria-current','location');else link.removeAttribute('aria-current');});}
addEventListener('scroll',markSection,{passive:true});addEventListener('resize',markSection);markSection();
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
    video.scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});
    video.focus();
  }
  if(video.readyState>=1)seek();
  else{video.addEventListener('loadedmetadata',seek,{once:true});video.load();}
}));
