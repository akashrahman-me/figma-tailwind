Could you please fix this code?
Please follow the following instruction.

-  You don't need to explain anything, just give me full fixed code.
-  Do not use 'style' attribute, instead use tailwindcss.
-  If you see we can get desired output using flex or grid then is flex/grid instead of position absolute.
-  make sure the code organized, also think about the layout if some class doesn't make any change to the layout or design just remove them.
-  If you see layout will never problem by using fixed value like width and height then remove it.
-  Please use semantic html elements.
-  Make sure it pixel perfect design. By making pixel perfect design, do not use position/absolute just make sure spacing get perfect.
-  Don't use fixed width/height if really we don't need.
-  If you see same element multiple time directly map it as we're using react.js and typescript. And if have text content then use it by storing it in a variable.
-  By using semantic html elements, make sure the layout will never problem. you can fix by using tailwindcss class.
-  Organize tailwindCSS className as much as possible.
-  maintain CSS over-specification problem, it's happens when you apply redundant or unnecessarily specific CSS styles that could be achieved more efficiently by it parent element.
-  provide me JSX code that I'll use it in my react.js project
-  Please do not, make any further improvement that isn't mentioned in jsx below.
-  Do not keep absolute positioning if not necessary.
-  If you found helpful to use gap for flex box element then use it instead of margin

-  Removed unnecessary absolute positioning.
-  Used flexbox for aligning items.
-  Removed fixed width/height, allowing the container to be more responsive.
-  Added padding and margin to space elements appropriately
-  You don't need text extract to a variable if that aren't required mapping situation.
-  Make sure you're use semantic html element and accessibility to ensure SEO friendly code.


<div style="width: 1440px; height: 830px; position: relative; background: #ECEFF5">
  <div style="width: 876px; height: 488px; left: 282px; top: 171px; position: absolute">
    <div style="width: 360px; height: 488px; left: 0px; top: 0px; position: absolute">
      <div style="width: 360px; height: 51px; left: 0px; top: 437px; position: absolute">
        <div style="width: 176px; height: 50px; padding-left: 55px; padding-right: 55px; padding-top: 14px; padding-bottom: 14px; left: 0px; top: 1px; position: absolute; background: rgba(235, 87, 87, 0.03); border-radius: 12px; overflow: hidden; border: 1px #EB5757 solid; justify-content: center; align-items: center; gap: 8px; display: inline-flex">
          <div style="text-align: center; color: #EB5757; font-size: 16px; font-family: Inter; font-weight: 500; text-transform: uppercase; word-wrap: break-word">Clear</div>
        </div>
        <div style="width: 176px; height: 50px; padding-left: 55px; padding-right: 55px; padding-top: 14px; padding-bottom: 14px; left: 184px; top: 0px; position: absolute; background: #2F80ED; border-radius: 12px; overflow: hidden; justify-content: center; align-items: center; gap: 8px; display: inline-flex">
          <div style="text-align: center; color: #F2F2F2; font-size: 16px; font-family: Inter; font-weight: 500; text-transform: uppercase; word-wrap: break-word">Submit</div>
        </div>
      </div>
      <div style="width: 360px; height: 413px; left: 0px; top: 0px; position: absolute">
        <div style="width: 360px; height: 360px; left: 0px; top: 53px; position: absolute">
          <div style="width: 360px; height: 360px; left: 0px; top: 0px; position: absolute; background: white; box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.05); border-radius: 12px"></div>
          <div style="width: 140px; height: 180.40px; left: 106.15px; top: 90.43px; position: absolute; border: 12px black solid"></div>
        </div>
        <div style="left: 0px; top: 0px; position: absolute; color: black; font-size: 24px; font-family: Inter; font-weight: 600; text-transform: uppercase; word-wrap: break-word">Draw digit</div>
      </div>
    </div>
    <div style="width: 360px; height: 413px; left: 516px; top: 0px; position: absolute">
      <div style="left: 0px; top: 0px; position: absolute; color: black; font-size: 24px; font-family: Inter; font-weight: 600; text-transform: uppercase; word-wrap: break-word">Predict digit</div>
      <div style="width: 360px; height: 360px; padding-left: 107px; padding-right: 107px; padding-top: 38px; padding-bottom: 38px; left: 0px; top: 53px; position: absolute; background: white; box-shadow: 1px 2px 4px rgba(0, 0, 0, 0.05); border-radius: 12px; overflow: hidden; flex-direction: column; justify-content: center; align-items: center; gap: 10px; display: inline-flex">
        <div style="text-align: center; color: black; font-size: 280px; font-family: Imprima; font-weight: 400; text-transform: uppercase; word-wrap: break-word">4</div>
      </div>
    </div>
  </div>
</div>