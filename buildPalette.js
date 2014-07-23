var Lab_CELL_WIDTH = 5,
    Lab_CELL_HEIGHT = 5;

var container = d3.select('#container');
container.style('display', 'inline-block');

function LabToRGB(L, a, b) {
  // Map CIE L*a*b* to CIE XYZ
  // Based on C3 implementation https://github.com/StanfordHCI/c3
  // An alternative conversion is available at http://rsbweb.nih.gov/ij/plugins/download/Color_Space_Converter.java

  // First map Lab to XYZ
  var y = (L + 16) / 116,
      x = y + a/500,
      z = y - b/200;

  var D65_X = 0.950470,
      D65_Y = 1.0,
      D65_Z = 1.088830;

  // Adjust the X,Y,Z values based on D65
  x = D65_X * (x > 0.206893034 ? x*x*x : (x - 4.0/29) / 7.787037);
  y = D65_Y * (y > 0.206893034 ? y*y*y : (y - 4.0/29) / 7.787037);
  z = D65_Z * (z > 0.206893034 ? z*z*z : (z - 4.0/29) / 7.787037);

  // Convert XYZ to sRGB where each sRGB value is [0,1]
  // This process uses the matrix found at http://www.cs.rit.edu/~ncs/color/t_convert.html#RGB to XYZ & XYZ to RGB
  var r =  3.2404542*x - 1.5371385*y - 0.4985314*z,
      g = -0.9692660*x + 1.8760108*y + 0.0415560*z,
      b =  0.0556434*x - 0.2040259*y + 1.0572252*z;

  // What does the following do?
  r = r <= 0.00304 ? 12.92*r : 1.055*Math.pow(r,1/2.4) - 0.055;
  g = g <= 0.00304 ? 12.92*g : 1.055*Math.pow(g,1/2.4) - 0.055;
  b = b <= 0.00304 ? 12.92*b : 1.055*Math.pow(b,1/2.4) - 0.055;

  // Integer representation of RGB [0,1] values
  var ir = Math.max(0, Math.min(Math.round(255*r), 255)),
      ig = Math.max(0, Math.min(Math.round(255*g), 255)),
      ib = Math.max(0, Math.min(Math.round(255*b), 255));

  // TODO: what does the following do translated into Javascript? Necessary?
  // return (0xFF0000 & (ir << 16)) | (0x00FF00 & (ig << 8)) | (0xFF & ib);
  return {R:ir, G:ig, B:ib, str:'rgb('+ir+','+ig+','+ib+')'};
}

d3.csv('colors.csv',
  function(d) {
    var color = {},
        rgb = LabToRGB(+d.L,+d.a,+d.b);

    color.L = +d.L;
    color.a = +d.a;
    color.b = +d.b;
    color.R = rgb.R;
    color.G = rgb.G;
    color.B = rgb.B;
    color.rgb = rgb.str;
    return color;
  },

function(error, colors) {
  // Get the sorted set of all L, a, and b values in the dataset
  var Ls = colors.map(function(d){return d.L;}),
      as = colors.map(function(d){return d.a;}),
      bs = colors.map(function(d){return d.b;});
  Ls = Ls.filter(function(d, i) { return Ls.indexOf(d) == i; }).sort(function(a,b) {return a - b;});
  as = as.filter(function(d, i) { return as.indexOf(d) == i; }).sort(function(a,b) {return a - b;});
  bs = bs.filter(function(d, i) { return bs.indexOf(d) == i; }).sort(function(a,b) {return a - b;});

  // Separate colors by L values
  colorsByL = [];
  for(i in Ls) {
    var L = Ls[i],
        subset = colors.filter(function(d,i) { return d.L == L});
    colorsByL.push(subset);
  }

  var Lcontainers = container.append('div').selectAll('div')
      .data(colorsByL)
      .enter()
      .append('div')
        .attr('id', function(d,i) {return 'L'+Ls[i]})
        .style('border', '1px solid #eee')
        .style('display', 'inline-block')
        .style('padding', '5px');
  Lcontainers.append('p').text( function(d,i) {return 'L*='+Ls[i]} );

  var LabChart_HEIGHT = bs.length*Lab_CELL_HEIGHT,
      LabChart_WIDTH = as.length*Lab_CELL_WIDTH;

  var LabCharts = Lcontainers.append('svg')
      .attr('height', LabChart_HEIGHT)
      .attr('width', LabChart_WIDTH);

  var aAdjust = -as[0],
      bAdjust = -bs[0];

  LabCharts.selectAll('rect')
    .data(function(d){return d})
    .enter()
    .append('rect')
      .attr('x', function(d){ return d.a + aAdjust; })
      .attr('y', function(d){ return d.b + bAdjust; })
      .attr('height', Lab_CELL_HEIGHT)
      .attr('width', Lab_CELL_WIDTH)
      .style('fill', function(d){ return d.rgb; });

  var LabChartsAxis = LabCharts.append('g')
      .attr('id', function(d,i) {return 'L'+Ls[i]+'_axis'});
  LabChartsAxis.append('line')
      .attr('x1', 0)
      .attr('x2', LabChart_WIDTH)
      .attr('y1', bAdjust)
      .attr('y2', bAdjust)
      .attr('stroke-width', 1)
      .attr('stroke', 'black');
  LabChartsAxis.append('line')
      .attr('x1', aAdjust)
      .attr('x2', aAdjust)
      .attr('y1', 0)
      .attr('y2', LabChart_HEIGHT)
      .attr('stroke-width', 1)
      .attr('stroke', 'black');
});