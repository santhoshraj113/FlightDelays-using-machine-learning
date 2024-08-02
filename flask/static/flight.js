const objects=document.getElementsByClassName("title");
const btn=document.getElementsByClassName("btn-div")[0];
const img1=document.getElementsByClassName("img-div")[0];
const content1=document.getElementsByClassName("content-div")[0];
const img2=document.getElementsByClassName("img-div2")[0];
const content2=document.getElementsByClassName("content-div2")[0];
const inputs=document.querySelectorAll("input")
const labels=document.querySelectorAll("label")
const select=document.querySelectorAll("select")
var titleobserver=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.classList.add("visible");
        }
    })
})
var imgobserver=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.classList.add("img-visible");
        }
    })
})
var contentobserver=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.classList.add("content-visible");
        }
    })
})
var imgobserver2=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.classList.add("content-visible");
        }
    })
})
var contentobserver2=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.classList.add("img-visible");
        }
    })
})
Array.from(objects).forEach(each=>titleobserver.observe(each))
setTimeout(()=>titleobserver.observe(btn),100);
imgobserver.observe(img1);
contentobserver.observe(content1);
imgobserver2.observe(img2);
contentobserver2.observe(content2);

