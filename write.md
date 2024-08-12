Outstanding. Now I want a another python function that will take 2 string argument and return string.

arugument one:

```css
.a {
  font-size: 20px;
  color: black;
}
.b {
  border: 1px solid black;
}
button {
  font-size: 16px;
  background-color: green;
  color: white;
}
.c {
  font-size: 18px;
}
.e .f {
  font-size: 20px;
}
```

argument two:

```html
<div>
  <p class="a">Lorem ip some</p>
  <b class="b">Hello World</b>
  <button>This is button</button>
  <strong class="a c">Hello gues</strong>
  <div class="e">
    <p class="f">Hello</p>
  </div>
</div>
```

and it will return

```html
<div>
  <p class="a" style="font-size: 20px; color: black;">Lorem ip some</p>
  <b class="b" style="border: 1px solid black;">Hello World</b>
  <button style="font-size: 16px;background-color: green; color: white;">
    This is button
  </button>
  <strong class="a c" style="color: black; font-size: 18px;">Hello gues</strong>
</div>
```

make sure, that will apply the css what browser behave.
