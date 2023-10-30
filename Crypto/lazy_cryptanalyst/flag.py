text = "bsxz xz om rxuvi. bsiri qri oqym gbsirz vxji xb, whb bsxz gyi xz oxyi. om rxuvi xz om wizb urxiye. xb xz om vxui. x ohzb oqzbir xb qz x ohzb oqzbir om vxui. fxbsghb oi, om rxuvi xz hzivizz. fxbsghb om rxuvi, x qo hzivizz. x ohzb uxri om rxuvi brhi. x ohzb zsggb zbrqxlsbir bsqy om iyiom, fsg xz brmxyl bg jxvv oi. x ohzb zsggb sxo wiugri si zsggbz oi. x fxvv. wiugri lge x zfiqr bsxz kriie: om rxuvi qye omzivu qri eiuiyeirz gu om kghybrm, fi qri bsi oqzbirz gu ghr iyiom, fi qri bsi zqpxgrz gu om vxui. zg wi xb, hybxv bsiri xz yg iyiom, whb ciqki. uvql xz q eqm fxbsghb wvgge xz vxji q eqm fxbsghb zhyzsxyi. qoiy."

newtext = ""

switch = {  'b':'t',
          's':'h',
          'x':'i',
          'z':'s',
          'u':'f',
          'm':'y',
          'o':'m',
          'i':'e',
          'q':'a',
          'g':'o',
          'v': 'l',
          'h':'u',
          'f': 'w',
          'y': 'n',
          'j':'k',
          'w': 'b',
          'e':'d',
          'l':'g'
          }
for char in text:
  if char in switch:
      char = switch[char]
  newtext += char
print(newtext)