# Flowers classification 

* Accuracy

<table border="0 px">
 <thead>
  <tr>
   <th align="left"></th>
   
   <th colspan="2" align="center">Train</th>
   <th colspan="2" align="center">Validation</th>   
   <th colspan="2" align="center">Test</th>   
  </tr>
 </thead>
 <thead>
  <tr>
   <th align="left">Model</th>
   <th align="center">Loss</th>
   <th align="center">Accuracy</th>
   <th align="left">Loss</th>
   <th align="center">Accuracy</th>
   <th align="center">Loss</th>
   <th align="left">Accuracy</th>
  </tr>
 </thead>
 
 <tbody>
 <tr>
 <td align="left">VGG16</td>
 <td align="center">0.0073 </td>
 <td align="center">99.89%</td>
 <td align="left">0.3853 </td>
 <td align="center">90.20%</td>
 <td align="center">1.0339</td>
 <td align="left">73.90%</td>
</tr>
<tr>
 <td align="left">MobileNetV2</td>
 <td align="center">0.1580</td>
 <td align="center">98.19%</td>
 <td align="left">0.2763</td>
 <td align="center">93.63%</td>
 <td align="center">0.5725</td>
 <td align="left">81.62%</td>
</tr>
<tr>
 <td align="left">ResNet50V2</td>
 <td align="center">0.1275</td>
 <td align="center">98.30%</td>
 <td align="left">0.2868</td>
 <td align="center">94.12%</td>
 <td align="center">0.5153%</td>
 <td align="left">83.09%</td>
</tr>
<tr>
 <td align="left">Xception</td>
 <td align="center">0.1331 </td>
 <td align="center">97.96 %</td>
 <td align="left">0.3179</td>
 <td align="center">88.73%</td>
 <td align="center">0.5829</td>
 <td align="left">81.62%</td>
 </tr>
</tbody>
</table>

_________________________________________________________________________________________________________________
* 17 flowers dataset are available from this link: 


<a id="raw-url" href="https://www.kaggle.com/datasets/saidakbarp/17-category-flowers">Download Dataset</a>

-----------------------------------------------------------------------------------------------------------------

* models are available from this link:


<a id="raw-url" https://drive.google.com/drive/folders/1-raii-CF07Vzw4IJOjDLdvMqiUOE2is0?usp=sharing">Download models</a>
    
 -----------------------------------------------------------------------------------------------------------------
 * Inference
  
  
     inference.py --data [path] --model [model name]

