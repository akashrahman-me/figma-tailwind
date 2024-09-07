Improve the following HTML by adding those instructions below.
- Adding semantic elements and SEO-friendly practices
- Use tailwindcss class instead of keeping style attribute
- Remove unnecessary styles/class
- Do not use fixed value width/height
- Do not use position absolute if it's really needs.
- Use aria attribute as much as possible.
- Make sure you can not change style, for example it has a font family and you can not change this font Family name as it change our design system.
- Do not include any explain, just give us the code.
- This is a ugly HTML structure, you can change it or even remove or add element as well as. Make sure you do not change overall layout/styles.


```html
<div style="width: 189px; height: 68px" class="inline-flex gap-7 items-center justify-center">
  <div style="width: 113px" class="inline-flex gap-3 justify-start flex-col">
    <div style="align-self: stretch; word-wrap: break-word" class="font-ibm-plex-sans text-right text-base leading-[2em] text-slate-700">الفيديو التعريفي</div>
    <div style="align-self: stretch" class="inline-flex gap-1 items-center justify-end">
      <div style="width: 16px; height: 16px; position: relative" class="">
        <div style="width: 11.67px; height: 11.67px; left: 2.17px; top: 2.17px; position: absolute" class="bg-gray-700"></div>
      </div>
      <div style="word-wrap: break-word" class="font-ibm-plex-sans text-right text-sm text-gray-700">مشاهدة الفيديو</div>
    </div>
  </div>
  <div class="rounded-lg bg-[rgb(243,_252,_246)] p-3 flex gap-2 items-center justify-center">
    <div style="width: 24px; height: 24px; position: relative" class="">
      <div style="width: 21.50px; height: 17.50px; left: 1.25px; top: 3.25px; position: absolute" class="bg-[rgb(27,_131,_84)]"></div>
    </div>
  </div>
</div>
```