import string
import random
from base64 import b64encode, b64decode

FLAG = 'flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'

#enc_ciphers = ['rot13', 'b64e', 'caesar']
dec_ciphers = ['rot13', 'b64d', 'caesard']

def rot13(s):
	_rot13 = str.maketrans( 
    	"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    	"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return str.translate(s, _rot13)

def b64d(s):
	return b64decode(s).decode()

def caesard(plaintext, shift=-3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def encode(pt, cnt=50):
	tmp = '2{}'.format(b64encode(pt))
	for cnt in xrange(cnt):
		c = random.choice(enc_ciphers)
		i = enc_ciphers.index(c) + 1
		_tmp = globals()[c](tmp)
		tmp = '{}{}'.format(i, _tmp)

	return tmp

def decode(pt, cnt=61):
    for i in range(cnt):
        c = pt[0]
        if c == '1':
            pt = rot13(pt[1:])
        if c == '2':
            pt = b64d(pt[1:])
        if c == '3':
            pt = caesard(pt[1:])

    print(pt)

if __name__ == '__main__':
    x = '2Mk16Sk5iakYxVFZoS1RsWnZXbFZaYjFaa1prWmFkMDVWVGs1U2IyODFXa1ZuTUZadU1YVldiVkphVFVaS1dGWXlkbUZXTVdkMVprWnJWMlZHYzFsWGJscHVVekpOWVZaeFZsUmxWMnR5VkZabU5HaFdaM1pYY0hkdVRXOWFSMVJXYTA5V1YwcElhRVpTVm1WSGExUldWbHBrWm05dk5sSnZVbXhTVm5OWVZtNW1NV1l4V1dGVWJscFVaWEJoVjFsdVdtUm5iMUpYVjNGS2IxWlViMWhXVnpFd1YwWktkbVpGWVZkbFIxRXdWa1JHVDJZeFRuWlhjRzlUWlZkclkxWlhZVk5TYmpGSFZsaHJaRkpVYjFOWmJsVXhWakZTVjFkd09WaFNNRlkyVmxjMVIxWldXa1pUY0d0WFpVWnpZbHBYWVhwVFYwWkhWM0JyVG1Wd2EydFdjSE5MVFVkSllsWnVaMWRsYm5OWldWUk9VMlV4VWxkWGJuZFVWbTl6V0Zad2QyNWtWbHAxVGxabldsWldWV0ZXYmxwTFZqRk9kV1pHYTJ0a01YTlpWbGN4WTJoR1NsZGxNM05yVW00MVdGbFVUa05OVmxwWVprVk9iV1ZXUmpWV2NIZHlaRzlLV0doRk9WVldjRkpVVm5CaFZtaEdaM1ZuUm1kVFpHTldXRlp3TVhwVk1XZDNVMjl2Vm1ReVVsWldiMmRUVlVaV2RGSndkMjFsU0VKSFZHOWFibFV4V25oUmJqRlhWak5yV0ZSdVdsTldNVko0Vm05T2EwMXdhMVpXY0dGdVpURlJZVmR4VWs5V1ZUVllWWEIzWkZkR2JucFdjSGRYWlZWYVlsWXlkalZXY0VwSFYzRmFWV1ZHY3pOWk1tRlhabkJLU0dSRk5WZE5WWE5JVm05U1IxWXlUblZOVm1kVVpXNWFWVmxVUm1SVU1WbDZWbkZhVGxKd1VsbFpNRlp1VlhCS1JrNVZiMXBOUjJ0TVdWY3hTMmRIVmtaYVJtZHJaREJ6Y2xaVVJtUldjRlpJVTI1YVdHUmpWbFZWYjFwNlVtOWFWMWR2WjJ4bFZrWTFWWEExUzFkSFJXSmtSazVYWlZock0xbFZXbVJXTWtaSlZHOVdVMlF6UW1SWFYzZFhaekZaZWsxVldsaGxSa3BYVkZablUxTkdXa2hvUm1kWFRWWktNVlp3WVhKa1ZrcFlaMk5DVjFaRmNucGFSRUV4VTBaYWRtUkdVbXhsVjJ0WVYxY3hORmxXWjFkV2NVcFhaVlJXVUZad1lYcFNNVnAyWkVkM1YyUmpSa2xXVjNkeVZuQkdkVkpVUWxWV00ydFFWbkF4UjFKV1ZuZGtSMnRPWlZaRllsWXhVa2RsTVZsaVZXOXJWMlZ2V2xoWlZFSjZabFp2VlZOd09VOVNiMWt5VlZjMVMyUXdNVlpPVlc5YVRVZFNTRlpVUVdGU01WcFpaRVphYkZkRlNrMVdSbHBrVkRGYWRsZHhSbFZsUmxwUFZtMUdTMU5XWjNaV2IxcHZVbTV6WTFVeGEzWlZNa1Y2WmtaQ1ZtVkhVVEJWWTBaYWFGZE9SbFJ2Vmxka1kxWktWakozWkdVeFdrZFhjVXB0VWxSV1pGbHVXbVJuVm5ORlVuRmFiMUp2U2pCVmNHRnVWVEF3WVZOdU5WZFdSVzVoV1cxQllWTkdTbmhXYjBwWVVqTnJXRlpHV21SWlZrNVhWVzluVjJWdU5WaFVWM2Q2VFZadWVsVnVaMWhTYjNOWVdYRnpTMWxXU25abVNFcFdUWEZPTkZVd1dsTm1NWE5IVkhCclRtVndhMUZXY0RCaFRrZFJZVlZ1WjJ0Tk1sSnlWVzlyVTJZeFduWmFSRkpYVm5CaFlWVlhNRFZXUjBwSWFFWnZWVTFXYzJ0V1ZFWmtaMGRHUlZKdloydE5iMFl6VmxoelIxTXhXbGRUY1VwWVpWZHJjMWxVUm5wV2IxbGhWVzVuV2xZeFNsaFdjRFZYVlRKS1IyWkdWbFpsUjFKMFdsVmFVMVp2V25kU2JqbFhaR05XV0ZZeWQzSmtNVnAzVTNGS1ZHVndhMlJVVlZwNlZVWldkMmhIZDIxbFIxSmpWa2RoVTFZd01YZGtSV3RYVmtWS2VWWnRRVEZTTVZaMlpVZHJVMUpWYzNsWFZsSlBaREExZGxadloxWmxWVnBVVkZabk5GWXhVV0ZXY1U1WFZtNXpXbFZYTlVkV2NFWjFVMjluWkZKRldsQldNRnBYWjFaYWRscEdUbGRTVm5Oa1ZuQnpTMDVHV1dKU2NVNVdaREZ6V1ZsdVZucFdNVkpYV2taT1QxSnZTbGRXY0hOVFpERktkV1ZqU2xaTlZrcElWbkIyWVZJeFduUlZiM05PVm05dk0xWlhNVFJXTWxKWVUyNXJiMUl6UWxSVmIxWjZWRVphZEZKd2MwNVdiM05qVm05cmNsWndSV05SYjJkVlZqTk9ORlJ2V2xkbU1rWklUMVU1VjJReWVtTldiMlpoWlRKR2RsZFlhMVJrTTBKV1ZtOW5jbWh2V2xWU2JuZHRUVlp6TUZrd1dsTlZNV2RJWkVWaFYyVllRbEJaYlVwVFowWmFkVmR3YjFOV01VcGhWMWN3WVdVeFJXRlhXR2RYWlZSdlQxUldXbGROTVc1NlZuQkdiRkp1YnpOVWIxcDJWbTR4UjFOdVVsWk5WMUpIV2tSR1YyWndUa2hvUm1kVFpESTVORll5WVc1TlJsbDZUbGhPVkdWdlduSlZibFprVjBaU1ZtUkZUbFJsUmxZMFZqSXhNRlV5U2taTlZGcFdaVVpLVEZZd1owdFNNVTUxV2taelYxWXlhMDFXVkVadVZERmFkbFZ4U2xSbFJrcFVWbkJoZWxkV1dsaG1SV2RYVFZaS1lsUnZXbVJYUm1kSWFFWlNWMlZIVVRCVmJVWjZVbFpHVlZadlVsTmtNMEkwVmxabU1XVXhXV0ZYYjJ0VlpHOUtXRlZ3TVU1b1JsWjBVVmhyVjJWRmMyTldNbUZQVmpKRlkxRnhhMWRrTVVwRVdXTkJNVll5U2tsVmNITlVVbTl6V0ZkWE1HRk9SbHBYWkROcmExSmpWbEJWYlVKWFRURnVlbFZ1T1ZkV1ZFWkhWakozTkZZeVJXRm1Sa0pYVFVkU1VGcEdaMHRTYjJkMldrWk9WMUpWYm1GV01uZFhaREF4U0ZadloxVmxSMUpyVlc1YVMxVXhXbmRvUjBaUFVuQlNXVlJWVWxkV01VcDFUbFpyVmsxeFVuVldibHBMVW05bmRsSnZXazVrYjFveVZrWmFaRk53VVdGa00zTmtVbTlLV0ZSVldubG9SbHAyV1ROcmEwMVdWalJWTWpWUFZrZEdkVmR1T1ZwV1JWcGtWRlZhZWxJeFozZG5SbEpzVm05eldsWnVaekJsTWtaM1UzRlNhMU5IWVZoV2JsWjFhRVpTZDJoSVowOWxSVnBpVmpJeE5GWXlTbGRUYmxKWFZtOXpkVlZ0UVRGV01XZDRWbTlLYkZKdWMxUldjREF4VVRGT1IxVnZaMWRrTWxKV1ZYQjNlbFp2VmxobVJXZHJVakJXTlZkdVVrOVpWbHBZVlZoblpGSXphMWRhUkVGaFYxWmFkbFJ3YjFkV2NVSTBWbkIzVjFZd05VZFViMnRXWlVaemExVnZWbnBXVmxaMldrUk9UbVZHV2pGWk1GWnVaVVpKWVZOdloxcGtNVm96Vm0xQllXWldTblZsUmxwdlpEQlpNRlp2Vm1SVU1XZFlVMjVyYlZKdU5WaFdiVXBTYUc5WllXUklaMWROVlc4MFZrZGhaRlV5U2tabVJsSmFWa1UxUTFwVldtNW5SMUpKVkc0NWJGSnZXVEJXTW5keVpqSktSMWR2WjFobFJscFlWRmMxVW1jeGIxaG9SVnB1VFZkU1lWWXlZWHBVY0VwSlVXNVNWMVpGU25sVlZFcFBWakZPV1ZwSGIxTlNWbk5aVmxkaFpHWXdOVmRtUldka1VrVktWRlJXVlRGVGIxcDNUVmhPVm1WR2MyTldNVkpIVmpBeFdHUkZZVlZsUjFKUVZqQlZNVlp1TlZaT1ZrNVRWbkZDVGxadlVrcE5WMDFoVTNGT2JWTkdXbFJaYmxwTFdWWlNWbHBFVWxSbFJrcFhXVlZXYmxZeFNuWlRiMXBXVFhGQ1NGbHVaMHRtY0VsalprWm5VMUpWYzBsV1dITkhWakpTV0ZKdWIxUmxXRUp6Vm05YWVVMUdXbmROV0hOdlVsUldXRlZ3WVdSV1YwcDNhRVpXVmsxSFVUQldSbHBYVmpGYWQwOVdVbGROUmxreFZrUkdaRlF4V2xkWGJscFBWa1ZhVjFwWGQwWk5WbFZoVjI1M1dGWXdOVVpXY0dGWFZHNHhSbVpGZDFoV1JWcHJWMVpuVTFZeFozWlhiMmRzVWpOclYxWndkMWRTTURWSFYyNWFhMUpZVWxWV2JVWkxVbTlhZDJkSVoxVmxSVFZKV2xWblIxWnVNVWRUYm10WFVqTnJkVlZ3ZG1GVFYwcEhWRzlyVkZKVmMwcFdiMmQ2VVc0eFdGUnhUbE5sUm5OMVZXNWFaRmRHVWxaWGJuZFZWbTlhWTFkWWMwZFdSMHBIVm0xYVZtVlVRVEZaVnpGR2FGZFdSMlZHYzFkTk1VbzFWMjVTUzFKd1ZrZGFTRXByVW05S1dWVnRUbkpXYjFwWVRWUkNUbEl3V21OV1IzZGtWakpHZGxkdlVsZGtialZFVkZkaGJsWXlSa2xVYjJkT1ZtNXpXVlp3TVRCWlZsbGlVMjV2VWxkSVFsZFVWVnBMVTBaVmVsZHZaMWROVmtwV1ZUSmhVMVl5UldOUmIwSlhUVlp6YTFwRVJrOVhSbHAyV2taV2EyaHZXbEJYVjJGeVZURlpZVlp4VW05U1ZHOVZXVzVXZGsweFdXSm9SVGxYVm05elkxa3dWbE5XYmpGWFZtMVNaRkp2YzFCV2JVWlBaakZTZFU1V1oxZGxTRUpNVmpKM1pHVXlSV0pXYm1kWFYwZGhWVmx3ZDJSV1JsSldXa1JTVDFKdlNtTldjR0Y2WkRBeFJWSnZaMXBXVmxwclZsUkJZVkpXVmxsa1JscHNaVzVLVVZaSFlXUlhjRkZoV2toS2ExSnZjMDlVVmxwNlUxWmFkMmRHWjFkTmJqVllWVEpoYmxaSFJuWlhiMnRWVmxaelRGVXlZWHBTTVdkNFZIQjNWMlZHY21GV2NHRlRVakZWWVZkdVdsaGtiMHBZVlc1V1MwMHhVbmRvU0VwdVRWWktZbGt3WnpSVk1EQjZVMjFXVjFaalJYcFpZMFpQWjBaT2VGTndiMU5sUlhOclYyOW5NR2N4U1dGbVJtZFlaR052VkZWdFFuWk9WbFozWmtWblZrMXVWalJaTUZaMlZqRktkbVpHVWxaa2JscFhXa1JHUzJkV1VuWlVjRzlUWkRJNGVsWnRSbTVOUmtsaFZXNXJWbVZIYTFSWmNERlRWakZTVmxad1JrNVdiMVl6VjI1V2JsVndSalpTYm1kWFpWaHJVRmxVUm1SWFJsWjFhRVpuYTAxWVFsRldjSE5IVkRGS1YxVnhWbXRTVkc5WVZtMU9jbFJXWjNWWGNEbHVUVlZ2TkZVeGEyNVZNa1ZpVlhGR1YyVkhhMVJVYmxwVFYwZFNSMVJ2VW14U1dFSlhWbTFKWVZJeFdrZFRjVXB0VTBoQ1pGUlhOVk5uYjFKMlYyOWFiazFYT1RaWlZWcDZaRlpuUmxOWWExZGxSMUkyV2tSQllXWXhVblphUmxwc1pETkNVRlpHVm1Sbk1VNTJaa1puVm1WSFVuWlZjSFl4VWpGdmRWcEVRbXRXVkVaWFdUQlNVMVl3TVVkWGNFWmtWbFp6YTFSd1lVZG1iMmQyVjNCdlYxWkdXbE5XTVZKSFZURkZlazFXWjIxU1ZuTlpXVlJLY2xVeFduZG9SWGRVWlVaV05GWndkMlJrTURGV1prWnJWazF4UWxoWFZtZEdhRmRTTmxOdloxZFNWWE15VmpGYVpGUXhXblpUY1ZaWFpVWmFXRlZ2WmpWT1JscDBVbkE1VkUxV2MxaFdWMkZrVmxkRmVtWkdhMWROUm5OclZXTkdWbWN4YzBaYVJrcHNWbTV6V0ZadFNqQk9SbWQxVFZWcmExSllhMnRXY0dGa2FHOXZWMWR1YzI5U2JqVmlXVzVuY2xSdlNXTlZWRVpYVmtWYWRGUldXa3BvUmxwNFVtOUtXRkl4U2xWV1JscFhXVlpGWVZwSVVtNVNZMjlRVlhCaFMxWXhaM1ZXYjJkWFVtNDFTRll5WVdSV2NFcFpWWEZ6VmxZemEydFdjR0Z1WmpGV2RscEZOVk5XY1VKT1ZuQXhOR1V5VFdGYVJXZFVaREZ6YzFWdlducG1iMXAyV2tkM1RrMVdjMVpWY0RWUFZUSktSbVZFVGxWTlZrcFVXVlpuUzJkSFJrVlViM05YVFRGS1lsWlVSbVJVTVdkWFYzRktaRkp2U25OWmJscDZVMjlhV0doR1oydE5Wa1l6Vkc5YVpGZEdaMGhWY1VaWFpWaHJhMVZ3WVZab1IwWkdXa1puVTJWRmMxZFdWbHB5WlRGYWRVMVZaMWhXUlVwclZuQmhTMlJHYzFaV1dHdHRUVlpLWVZZeVlWTlZNVXBYWmtaQ1YxSXphM1JVVmxwa1UwWlNkbVJHV210TldFSlZWa1pXVTJZeFJXRlhibWRZWlVkU1VGWndZWHBOVmxWaVRWYzVWMlJqUmxoVk1uTkhWakpLU0ZWdlFsZE5jV3RNVm05YVIyWldTbmRuUlRWT1VuRkNWbFl5ZDJSV01rMWhWSEZLVGxaWFlWaFpibHBrVmtadlZWUnZUbTFXYjBwV1ZWZGhibFJ1TVZaWGIydFlaREZhZFZaSGRucG9WMVpIV2taYVRsWnVjMDFYVm1jMFpERktkMUp1VmxobFdGSllWakJXUzFJeFozWldjSGRyVFc1eldGWkhZVzVXUjBWaWFFYzVXbFpGYzNWVVZFWnVabFpLZFU5WGQxZE5Wbk0xVm05YWNtUXlSblpYYmxwc1RUSnJXVmx2YTFOb1ZuTkZVbTQ1VjAxWVFrcFpibWMwVmpGYWRtWkhPVmRXWTBZelZXMUdSMll4WjFsbVJsSnJUWEZyYTFkWFlYSlZNVWxoVlc5YVYyVkhVbGhVVmxaNmFGWnVlbFp3Umxka1kwWklXVzVTWkZkR1drWlRXR2RXYUc1eldGcEZXbE5tY0VaSFZIQnJhMDFIT0hwV2NEQmhhSEJXUjFkdWExVmxSMUp5Vlc5clExWldXblpXY0VaVlVuQjNOVlJ2YTA5V01VcDFaVVJhVmxZelFtdFdjSFpoVWpKT1JWSnZaMWRsUm5NMVZrWldaRlV4V2xkVWNVcFhaR05XV0Zad05VTlVWbWRWVW05blUwMVZNVFJXY0RWWFZuQktkVTVZUmxabFdFMWhWVzFHWkZaV1NuaGFSbFpUWlZoUk1sZFVRbkptTVZsaFZHNWFXRlpGU2xkV2NHRmtUVEZhZFZkd1JtNVdialZoVm5CaFYxZEdTblptUlc5WVpERktSRmxqUmxkU01VNVpaRVpTYkZaR1dsUlhWekV3VWpBMWRtWkdaMWhsV0ZKVVdXNVZNVll4Vm5kT1ZtZFlVakJ6U0ZVeWQwOVhjRXBIVjIxT1ZXVkdjMHhXYjFwSFoxWnpSazVXVGxkU1ZuTmFWbTltWVU1R1dXRlZjVTVYVjBkU1QxVXdhME5XYjNOWVowVjNWRlp2VmpOWlZWcHVWWEJLUmxkdloxcFdWa3BVV1ZWblMyWnZUblpXYjJkVFpVaENWVlpVU2pSV01rMWhWRzl2WkZKdU5WaFdiVXB1VGtaWllWcEVVbTVOVlRWWlZuQmhjbFV5U2xaWGIxSlZWbFphYTFad1lWZG5SMVpIVkc5T2EyaHVXa2hXY0RGNlZqRlZZVmR2Vm14U1YxSldWbTlhWkdodmIxWmFSVGxUVFZaellsWXlZWEprUlRGWlVXOW5WMVp2YzNSYVZXZFhWakZTZFdWR1RtdE5WWE5oVm5CM1YxTXhVV0ZXY1U1WFpWUldkbFZ3TVRCT1JscElUbFpuYkZJd1ZqUlZjSE5UVm5CS1IyWkZZVlZXYjNOaldUSmhaR1pXWjNaWGJqVlhUVEpuTkZad1lWTlNNa1ZoVjI5blZXVkhVbFZaYmxwTFpURlNWbGR3UmxWU2NVSklWbkF4TUZaSFJqWlNibTlYVWpOcmRWWlVRV0ZUUmxaMVQxWm5WMUpWYzNKV2NIZGtVakZuUmsxV1dsaGxXRkpQVlc5YWVsTnZXbFZTYjJkc1RWWktZMWR1Vm1SWlZUQmlWVzlHVjJWVVJsUldSRVoyWmpGbmRXWkhZVmRsUlhOSVYxWldVMVl5U2tkVWJscFlaVVphV1ZadVZucFRSbWRYVjI0NVUyVkZjMk5XTW1GVFZqRm5SbE51YTFkU2IxcFlWRzVhVDJZeFozUlhiMnRyVFRCS1ZsWlVRbVJXTURWWFZuRk9WMlZVYjFoVmNHRjZVakZ2VmxWd1JsWk5WbTgyVlZkelYxWnVNVWhrUm10VlpERnpTRlp3TVZOVFIwNUhXa2RyVGxkRlNrdFdiMUpIV1ZkUllXVkdaMWhrTW1GWVdXNVdTMVpHV1hwYVJ6VnVUVmRoVmxWWE1UQldiakZXVGxaclYyVllVbmxaVkVGaFUwZFNSVmR2WjA1bGNHdE5Wa2RoWkZad1VXRmFTRTVZWlVaYVdGWnVaek5OUmxwSFZtOWFiMUp1TlZoVk1uZGtXVlpLVm1aR1oxVldjR3RFVm5CaFYyWXhXbFZXYjFKT1pVWnlZVlp3TUhwb1JscElVMjVuVkdWR1dsaFVWVnBrVjBaVlltaEZkMWROVmxveFZuQXhORll4V2xkbVIydFhWak5yYTFWalFXRlhSa3A0VTI5YWEwMXhhMk5XVjNOUFVUQTFWMlpHV210VFJUVllXVzlWTVZkdmIzVldibmRYVW01eldGWXhhM3BXYjFwMlYzRktWbVJ1V2xoWk1uWmhWMGRTUjFadloydE5XRUpOVm5BeE1GbFhVV0ZYY1U1VVpERmFVMWxZYzBkV1ZscDJWMjUzYjFadlZqTldWM2RQVkc5YWRtVkVUbGRXTTFKalZqSjJZVmRIUmtaUFZsWlhhRzlhV0ZkdVVrZFRNbEpZVTI1YWJWSnZTazlWY0dGMWFGWmFkbFZ1WjJ4TlZYTllWa2RoWkZZeVNsWlhiMUphWkRGemExVnRSbTVtVmxKMVowWm5WMDFWYzFsV01uZFhWakZTZGxOWVowOVdWMnRYV1ZkM1MyaHZVblpXVkVaWFpVZFNZMVl5WVZkbFIwVjZaa1Z2VjJWR2MxZFViMXBQVWpGU2VGTndhMU5OTUVwalYxWlNTMVF3TUdGWGIxWlZaVWRTVlZadFJtUldNVlozWjBSQ1ZrMUVSa2xXVjJGWFZqRktSbE54Vm1SV1ZuTmlXa1JLUzFOV1duWlhjRzlYVFZWelYxWXhabnBOVjFGaFUzRk9iVkpXYzFoWmJsVXhabTlhZFZadWQxSk5WbFl6VjI1cmJtUndTbFpPVkVKV1pWaFNhMWxXWjBab1IwNUhWWEJHVTJWRmMwMVdWekUwVkRKU1IxVnhVbXhTTTBKWVdWUkpOR2N4WjFob1JtZHNUVzVhU0ZVeVlXNVdWMFZqVVc5clYyVkdTbU5VVlZwV2FGVTFXR2RHV2xObFJsa3hWa1JHVjJZeFdrZFRXSE5TWkdOdldGbFVSbGROTVZKV1drVjNiVTFXV2pGVk1tRlRaRmRGWVdVeloxZGxWRll6VlZSR1RtaEdaM1ZhUmxaclRUQktWVmRYZDJSWlZsRmhWMjlXVkZaRldsQlpibFo2VmpGelJsWllhMWRTYjNOWVZYQnpVMVp1TVZoa1JFNVhaREZ6WkZwWFlVOW1WbFoyVjI0MWEyVkdjMDFXYjFKTFRVWlpZbE5ZYTFSbFJuTjBWVEJuY21ZeFZuWlZibHBPVW05S1YxZHVhMjVrTVZwMlYyMUdXbGRJUWt4V1ZFcEdhRzlHZFZwR1drNWxiMGxqVmtkaFpGTXhXblZQVmxwa1VsUldWRlp1Vm1SVVJtZFlUVlJTVkdSalZsaFhibXRMVjBkS1JrNVZPVmRsUjJ0NVZHOWFWbWN5UmtkYVJsSlRaR05XVjFaWE1HRm1Na1pJVWxocmJWSllRbVJXTUd0RFZrWm5WMWR3UmxSV2IzTmlXVlZhVTJSWFNsaGFSRkpYWkc1dVlWVnRSbFpvUms1MldrZHJVMVp4UWxaV2JVSmtWM0JXUjFkdVoxWmtNbEprVm0xQ1YwMHhXblprUjNkYVZsUkNOVmxWVms5V01rcElaRVZTWkZKV2MxQlZiMXBUWmpGR2RscEdUbGRsYmtwTVZuQmhjbWN4VVdGVGNWSlhaVzlhVkZsdlp6UldSbEpXV2tjNVZFMVhVbGxhUlZwdVZrZEtSbGR2YjFWbFIxSklWbkF4UjJadlozVlBWbk5PWlc5S05sWlhNVFJuTWxKWFVuRktiRkp2V2xSVVZFWktUVlpuZGxad2QxVk5Wbk5qVlRKaFYxVnZXa2RUYmpsWFpVZHJRMVJXV2xab1JscDBVVzlPYTJodVdraFdjREUwWnpKR1dGTnVaMWhrYjBwWVdXOVNRbWhHVW5kTlZrNVRWbTQxWWxZeVlVOVViMHBJWmpObldGWmpRV0ZaYlVFeFUwWktlRlJ3YzFOWFJVcGlWbTFDWkZsV1RrZFZiMVpVWkdOV2RWUldWbnBYYjI1NlpFYzVWMDF1YzJKV01WSkRWakZLZG1aSVNsWmtibHBQV2tSR1pHWXhWbmRsUjI5VFpETkJNVlp2VWt0TlIwVmhWRzVuVjFkSFVsUlpWRVprVmxaVmVscEVVbFJXYjFwaVZuQXdNVlF4V25aV2JVNVZWbGRyWTFsVVJtUm5SMFpHYUVkR1YxWXlhMWhYYmxKSFZURlpZVlJ4U20xU2IwcFVXbGN4TkZadldsVlNjRVpXVFZWdk0xUldWblprVmtsNlYyOVNWMlZIYTBSVWJscDZWbTlhZFZwR1oyeFdibk5aVm0xS01HUXhXV0ZYYjJ0dlVtOXpWMWx2YTNKVlJsWllUVlZhYmsxdU5VWldjR0ZQVmpGYVNHaEZZVmRXUlVwWFdsVmFibFl4VW5WV2IwcFhVbTl6V1ZaR1duSlJNVnAyVm05bldrMHlhMVpXY0hZeFUyOVdkMmRHVGxkU2IzTlpXVlZWTlZkR1duZFVXR3RYWkRKU1dGWnRTa2RTYmpWV1RsVTFVMUl6YTA5V2IyWjZUVmROWVZwRmExWlhTRUpUVmpCblUxWkdXbmROVms1UFZuQlNXRmxWVm01a01WcDFaa2h6VjFJelVreFdWMkZrVmpGbmRXaEdjMDVXTVVweVZsUkdWbWhHVGxoU2JtOVRaVVphV0ZWdlVsZFZSbHAyVlc1T1dsWnZTa2haVkU1dVpGWktWMlpJVGxaTlJuTnJXVEJhVjJkWFRrWlVjR3RzVm05ek5WZFdVazlrTWtaMlYzRlNWbVF6UW10V2NYTkhUVzl6UlZKdlRsTmxWVnBKVkc5YWVtUlhSWHBtUlhkWVpERnpkVlpVUmt0bU1WSlpXa1pDVjJWRmMxVlhWM2RrVXpKU1YxVnZXbGRsVlZwVlZYQmhSMDVXVldKblIzZFhUVlp2TTFSdlducFdNREY0VlZoblZtVlVSbFJXY0RGTFVqRm5kbVpGTlZOTk1tdEpWbTlTU2sxWFRXRlVibWRWWlc5S1ZGbHdNWEpaVmxwMldrZDNUMUp2VmpSV01uWTFWVEF4VmsxVVZsZFNNMUo1Vm01blMyZEdjelpTYjJ0c1VqSnJTVlp2VWtkVU1XZEhVM0ZXV0dWR2MwOVVWVnA1YUVaYWRGTnRRbTVOYmpWWFZGWldkbFV4WjBob1NFNVhaRzQxUkZaRlducFdiMXBaWkVaU1YyUXpRa2hYYmxaa1ZURlpZVk52YTJSb2JuTlhXVlJHUzFOR1ZuZE5Wa3B1VFVSdlYxVXlZVXRXTWtWaVp6TnpXRlp2U2tSV1ZFWlRVakZuV1dSR1dtdE5NRXBaVm5CaFUxVXdOVWRXY1U1WFpWaFNXRlZ3WVhaTk1WcDJaRWQzV0dSalJraFpNR2R5Vm00eFNHUkliMVZXYjNOTVdUSXhUMUpXU25WT1ZrNVlVbFZXTkZadlVrZGtNVTFoVkc1YVRsWldjM05WYmxwNlZrWnpXR1pqUmxOTlZuTmhWWEExWkdWR1NuWmxSRlpWVm05YWRWWlVRV0ZXTWtwRlZXOXpUbFp1YzBWV2JtYzBVekpTUms1V1oxVmxWMnQyV1c1YWVsTldXbmRuUm1kV1RXNDFZMVV5WVc1V1IwcFlhRVpDVjJWR1dtdFdibHBrVWpGbmQwOVdVbGRXUlZwSlZtNW5ORll4VldKVGJscHNhRzVhV0ZSWE5WTldNWE5GVTI5blYyVlZOVXBaVlZwa1pFZEZlbVV6WjFkV1JVcDBXbFZhVTJZeFozWlhiMnRzVmpKcmExWkdWbkpSTVZKSFprVldVbVF5VWxsVmNIZDZhRVpXV0daalJsZE5Wbk5aVmtkelYxWXhTbmRVV0d0a1VtOXphMVV3WjFOU01XZDNaa2RyVG1Wd2ExZFdiMXBUVVRKTllWWlliMVpsUjJ0WFdWUktORlF4V25aYVNITnVUVlp2TlZwVldrOVZNa3BHVGxSR1ZtVlVWbFJXYjFWaFVtOW5kV2RHV2s1U01tdFlWMjlhWkZReFNsZFRjVXBZWlZoU1dGcFhZVlpvVm1kMVYzQkdXbFp1YzJOV1IzZDJWakpHZGxOdmIxcFdSWE41V2xWYWRsZEhVa2RhUm1kc1VsWnpaRlp3TVRCa01WbGhWMWhuVDFaWVVsZFpibWR5VFRGYVNHaEZjMjVOVjFKaFZsZGhlbFJ3U2tabFkwWllaVVp6ZVZWdFJtUldNVkoxWlVkR1RrMXdhMWRXVjJGa1YyNHhSMlF6YTFkV1JscFZXVzVhWkdoV2MxWmtSazVYVW01elIxVXlOWFpXTURGSFZtMU9aRll6YTFOYVZWcGtabTl6UjFSdU5WTlNiM0l3VmpGU1ExVXhUV0ZYYm1kVlpESmhVMWx1V2t0bWIxcDFWM0ZuYTFKdlZqTldNbmQ2WkRBeGRVNVliMXBrTVZwTVZtMUJZVkl4VG5WbVJtdFhVbFp6Y2xkdlZtUldjRkY2VFZaclUyVllRbGxWYlVweVZtOWFkVlZ1VGxwV2JqVmpWa2RoY2xaSFJXSmtSVGxWVmtWeU1GWXhXbGRtTVZwNFZHOUthMmh2V2pWV2JVbzBWakpHUmsxV1oxUmtZMVpYVkZaYVpGWXhjMFZUYmpsVFpWVmFSMWx1WjNKa1JURkpVVzlTVjJReFNraFdSRXBUVmpGYWVGWndiMU5sU0VKVlYxY3dZVTVHVFdGV2NWSlBWbFZ6ZFZSWGQxZE9WbHBJVGxkM1YyUmpRalJXTW1Ga1ZtNHhWMWR4V2xWa01sSk1WbkJoWkdaV1ZuZG1SbWRYVFZWelRGWnVXbGRsTVZWaVZIRlNWRmRIYTFaWldITlhaa1p2VlZOdFVsZE5WbHBqVmxkM1QxWkZNWFpYYjJkYVpESlNZMVl3WjBab1YwWkdaMFpuVGxZd01UUldjR0ZrVlRGWllsUnVXbVJTY0ZKVVZuQjNlV2N4V2xoTlZGSlRUVlp6UjFSdmEwdFdjRVZqVVhCR1ZWWlhVVEJVVmxwa1puQkdTVlJ2WjFObFZrbzJWbkF3WVdjeFduWlRiMjlTVmtWS2ExVndNVk5VUmxaM2FFaE9XRkp2U21OWlZWcFhWakpHTmxaeGExZGxXRkpZV1dOR1QxZEdWblpXYjFKclRWaENWbGRYWVZabk1sWlhWbkZPVm1Rd05YSlpibXREVWpGbmRGUndkMWRTYjNOaVdUQldjbFp1TVZoa1JXZGtWak5yVEZZeFducFNiMDUyV2tVMVUwMHlhMHhXYjFKSFpERkpZbFZZYTFkbGJscHpWWEF4Y2xaV1ZuUlJjRVpTVFZkaFkxWndZVzVVTVVwM1owUk9WbVZZVW1OV1IyRkxWbFpLZDA5V2MyeFhSMnRNVmtkaFpGbFdXbmRTYmxwc1VtNUtXRlZ2Vm5wVU1WcFZVWEE1VjAxVldtTldSMkZYVmxkS1dWRnZhMWRsUm5OTVZXTkdWMll5UmtkYVJsWnNWbTl6V0ZaWE1UQk5SMFozVWxoelVsZEhhMWRhVjNZeFUwWmFWVkp1ZDFSU01EVkhXVlZhVTFVeFdrWldiVkpYVm1OQllWbGpSa2RtTVZKNFZtOVNiRkpVVm1KV1YzZGtXVlpPUjFWdldtdFNWMUpZVkZaYVMxZEdWbmRvUms1VlpHTkdXbFZYWVc1WFJscEdWM0JyVm1WVVJsaFZNVnBYVmxaS2QyWkdUbE5XY1VJMFZtOW1ZVTFHYjFkVWJtZFZaVVphV0ZsVVJucFVNVloxV2tST1RtVkhkelZhVlZwUFZHOWFlRkZ4YjFwV1JUVXpXVzVhWkdkSFZrWmtSbHBPVm05eldWWndZV1JWTVZwWFUzRktWR1ZGTlZsVmIydERWa1phZFZWdU9XeE5WVEUwV1c1YWRsWXlSV05SYjFKa1ZqTlNTMVJXV21SbVZrcDRXa1pTVjAxV2MxaFdSRVpYWkRGYVIxZHhVbFpsYmtwWFdXNWFTMVZHVW5aWGNFWlhaVWhDU2xaWFlWTldNa1ZqVVc1dlYyVkhUalJhVnpGWFZqRk9kbGR3YjFOV2NVSnlWMVpTVDFGdU1VZFhibWRYWlVkU1ZsbFljME5OTVZaM2FFWk9WMVp2YzBkVWIxcEhWbFphVjFkd2ExWm9ibk5RVm0xR2VsSnZUbmRvUms1WFpVaENaRlp2WnpCV01rMWhVM0ZPV0dReGMxbFpWMkZMVmpGU1YyUkZUbFJTY1VKWlZHOVdibVJHV25WbVJXZGFWbFpLVkZsVlowdFdWbHAyVm05blUyVklRbFZXVjNOSFpqRm5SMVZ2YjJSU2JqVnlWRmMxY2xkdldXRmFSRUp1VFZVMVdGbFVUblpWTWtwM1ZXOW5WMlZZVFdGV01WcGFhRmRXUm1kRk9WZGtZMVkxVjFSQ1UxVXlSblpYYjFac1VsaFNWbFp2V2xkT1JscDBVbTQ1VTFadWMySlZNbUZrVkhCR2RsWlliMWRXTTFKVVZXMUdTMll4V25oVmNFWlRWakpyVlZadFFuSlJNVnBYVmxobmExSlZOVmRVVmxwWFRrWmFXRTVXWjJ4U01ITmpWakpoYmxad1NrZFRibEpWVm05ek0xa3lZVXRtY0VwSFprVTFVMlZ1UmpWV2NHRmtWakpOWVZaWWExUmxibk4wVlRCV2VtWkdXblprUlVwT1ZtOVdORmR1VmpCV1IwcEdUbFZuV2xaWGEwaFpWMkZMWm5CT1JWVnZaMnRrTW5jMFZuQmhibEp3VVdKVWJscHVVak5yV0Zad1lWcG9iMXBWVVc5T1VrMVdTbU5aYmxwdVpHOUtXVkZ2Vmxka01YTk1XVlZhVm1oSFJrWmFSbEpPWkdOV1YxWlVTVEZsTVZGaVVsaHpVbVZHU21SV2NYTkdaekZ6VjFwR1oxaFNiMG94Vm5CaFUxVXhTbFptUmxwWFpWUkJZVlZqUms5V01rbGpaa2RyVTFaWVFsWlhWM2RXVFZablIxWnhSbEpsYmpWV1dXNW5VMmh2YjNSVWNVNXJUVlp2TmxaWGQyNVpWbGxqVkcxU1YwMUdjMHhaTVZwSFpuQk9SMXBHWjFkTmIwWTJWbTVTUjFsWFNXRlViMnRYWkRKaGMxVXdWbVJXUm05MVZuQkdWbFp2V21GVlZ6QXhaVVphZGxadFRscGtNVnByVm01blIyWXhaM1pXYjJkT1pYQnJWVlpHV21SVWNGRmhWM0ZPVldWWWExaFVWbXREVkZaYWRscEljMjlTY0ZKSlZUSTFUMVpYUldGbVJtdFdaVVpLUkZSdlducFNNVnAxVDFkaFYyVklRa3RYVjNkWFpURmFSMU51V2s5WFJVcGtWbTFPVDAweGMxaG9SWGRYVFZaS1lsZHVXbE5VY0VZMlVsUktWMVl6YTNsWlZFWkhaakZLV1dWR1FsZFhSMnRqVm5BeE5HY3hVV0ZYYjJkWFpXNDFXRmx1WjFOTlZtZDFWbkZuYkZKdU5VZFpNRlo2V1ZaYWRsZHVhMlJTUlZwUVZYQjJZVlp3U2tobVJrNXJUVEJKWVZad01UUldNVnAzVlZoblVGWndVbGhaVkVwVFZqRlNWMXBHVGxoV2IxcGpWbkF3TlZSdlNYcFhjVzlXVFhGU00xbFhZV1JtTWs1RlVtOWFUbEp4UWt4WGIxcGtVekZhZDFOdVoydFNNMnRVVm5CaFdtaHZaM1pXY0hkdVRWZGhXRlV4YTI1Vk1rcElWVzl2V2xaRk5VUmFWbHBXWnpGYWQxSnZVbXhTVkZaWVZqSjNWMWxYU2tkVFdHZFBWbU52V0ZWd1lYcFdSbHBJVFZaT1YyVkhVbU5WTW1Ga1ZHOUpZMlJGYTFoV00ydHJWa1JCTVZJeFRuVlhjR3RUVmtaYVZWWkdWbVJUTVZKSFpETnJXR1JqYjFaWldITkhUVVp6Umxad09WZFdibk5aVjIxT2JsZHZXalpXYms1a1ZqTnJZbHBFU2tkVFJrcDJWVzluVjJWSVFsaFdiMlpoVGtaSmVrNVdaMlJTYjNOWldWZGhlbGxXVWxob1IwWlBVbTl6V1ZSdmEwOWtSa3AxWmtodldsWldWV0ZXTUdkTFptOW5WVkZ2WjFkU1ZYTXlWbGN3WVZZeFduZFRibXRzVW05S1dGbFVUa05UTVdkWFdraHpiMUp2VmpOVU1WcHVXVlpLVlZadU9WVldWbHBZVkZSR1YyWXhaM1ZuUjJ0cmFHOWFOVmRYZDFkbU1rcEhWMjluYlZKRldsaFdiVTVEYUc5WllWZHZUbGRXYmpWaVZuQXhjbFJ2VGtoa1JYZFhUWEZDUkZkV1oxSm5NREZXWlVaT2JGSnhRbFZXVjJGdVRrWkpZV1ZJVW0xTk1sSjJWbTFHUzFkdmIxWldjRVpYVWpCellsWnZhM1pXY0VwSFUyNXJXbFp3VWtoYVJscEhWMWRPUjFadloydG9iMXBLVm01YWJXaEhWbmRXY1U1VVpXNXpjbFZ1V21SVlJtOVZVbkZPVGsxWGR6UldNalZQWkRGYWRtWkdaMWRsV0d0alZsUktTMUp3U2tWVWIxWlhaVVp6V1ZaSGQyNVdNVnBYV2toV2ExSlVWbFZWY0dGNmFGWmFXRTFVUW10TlZWcGpWbTlyZWxVeVJuWlRiMmRWVmxkU1ZGVXdXbnBXTVdkM1owWktiRkpVVm1SWFZFSmtWVEZuUjFOeFZsSmtNMUpYVm5CaGVtWnZWV0ZhUm1kdVZtNXpXbGx1V2s5V01WbGpaRVZyVjFZelFsQlZiVVpXYUVkRlkyUkdhMnROY0d0V1ZuQmhVMUl5UmtkWFdHOXVVMGRTVkZsdVdrZE5NVmxpYUVabldHUmpSbUpaTUZKSFdWWmFWMWR4YzFwV1YxSlFXa1puUjFOWFJrZFhjR3RPVjBWS1RsWXhXbE5SY0ZaSVZtOXJWMlF5WVZoWmJtZHlWbFphZFZad1JtMVdiMVl6Vm5BMWJtUkdTblpUYjJ0WFpWaFNkVmx1V21SV2IxcDBWRzlhYkZKdmN6SldSbHBrVWpGYWQxUnVaMVZsUlRWWVdXNXJRazFXV1dGWGIyZFhUVlp2TlZVeU5WZGtiMHBYWmtjNVYwMUdXak5WWTBaa1psWk9kV2RHVGs1U1JWcExWMWQzWkdReFowaFNXRzl1VFRKcmExVndZV1JrUmxwWVRWWm5WMVp1V2pGWmJscGtaRmRLUjJaRmMxZFdSVnBZV1cxS1YxSXhUbmhUYmpWWFpVWnpWMVp0UW1SWlZrNTJaa1phVm1ReVVsVlVWbHBMVWpGdlZscElUbFZsUm5OWldsVmFVMVl4U2xoVWJWSldUVlpXTkZZeFdrdG1NVlozWlVkdlUxZEZTazFXYjJkNlVUSlJlazFJYTFaWFIxSlVXVlJLVTFaV1VsVlRiVkpZWlVaV00xWlhkMjVWTWtwSFprVm5XbVF4V2pOV2JVRmhabFpLZFdSSFJsZG9iMXBKVmtkM1pGUXhaMGRUY1ZaclVuRkNXRnBYTVRSV1JscDFWM0JHVmsxVmJ6UldiMnR1VlRKS2RsTnZWbHBsVkVVd1ZqRmFibGRIVFdOa1JscE9WbFJXV1ZadFNURldNVkoxVFZWblYxZEhVbGhWY0dGTFVURnpWbGR3UmxObFZUVkdWbGN4UjFSdldXRlRibmRYVW05emRWWkVSazluUms1NFZHOVNWMUp2YzFGV1Z6QXhVVEZhZGxaeFNsWmtNRFYyVlcxQ2VsWXhWbmRuUjNkclpVWnpZbGt3VlRWV01rcFpWWEZXWkZaalJsQldiVVpYWm5CT1IxVndiMnhTY1VKNVZtOW5OR1V5VVdKU2NVNXNVMFZ6Y2xSVVNsTldWbFowVkc1T1ZVMVdjMVpWVm10eVZHOWFkV1pFUmxwa01WcE1WbTVhUzFZeFoxVlNiMmRYVWxWellsWlVRbFpvUms1WFUzRk9aRkl5WVU5V2IxcDZWRVphZDJkR1oxcFdiMVkwVmtkM1YxVndSalpTYjFaV1pHNXpWRll4V2xabk1WWjFWSEJ6YkZJeFNsaFhWbFp5VlRGYVYxZHVaMWhrTWxKV1ZuQXhjbEV4YzFaWGJuZHRaVWhDUjFReFozSlViMDVHVTI1M1dGWkZXbGhaYlVwU2FFWmFXVnBHVGxkU1ZYTlZWMVpTVDFVeVRsZG1SbXR1VW5CU1VGVnRSbVJXTVhOR1ZtOW5WMUl3YzBkVWIyWTFWbkJLUjFkeGMxZFNZMFpVVm5CaFpGZFdjMGRYY0dGcmFHOWFUbFl5WVdSV01rMWlVbTluVkZkSFVuSlZiMnREVjBaYWRscEZPVTlXY0ZKV1ZURlNSMWR2V2xWU2JscGFaREZaTUZaVVFXRldNVTVWVW05elYwMHhTbFZXVkVaa1ZURmFkMU51V21SU2IwcFVWbTVXWkZadloxaE5WRUp0VFZWYVlsUldWbVJYUjBWalVXOXJWVlpXV210V1JWcGtWMGRTU1ZSdmExZGtNMEpJVjFkM2JtY3haMGhTV0d0dFVtOUthMVp2V2t0U1JsWjNhRVZ6YmsxRWIwWlZNbUZUVmpGS1ZtUXpaMWhXYjBwTFZHOWFaRkl4Vm5aa1JUbFhWMFZLV0Zad01XTk5WazVYVm5GU2JsTkZOVmxWY0RFMGFGWnZkVlp4VGxkU2NGSktWVmQzZGxkd1NrZFhjWE5WVm05elRGcEdXbnBTY0U1SFZYQnJUbVZGYzFsV2NIZGtWakpGWVZOdloxVmtNbUZ6VlhBMVExWldWblZXYm5OdlVtOXpWbFZYTVVkV01rcElaMFJTVjJWWVVtdFdjREZMWjBkV1NWUnZjMDVTYm5OUlZrZGhaR1F4U25abE0zTnJVak5DV0ZwWFlXUlRNV2QxVlc1S1QxSXhXbGhWTW1GWFZYQkdkVmR3UmxwbFdGSklWRzVhYmxaV1JuZFNiMUpUWkRKNlkxWndNWHBTTVZWaVVsaHZhMUp2V2xkVVZ6VlRaRVphZGxkdlRsZGxTRUpIVlRJeE5GVXhXblptUm05WFpERnphMVpVUmxObU1YTkdWM0JyVTFKdWMxQldiVUp1WlRBMVYxWllaMnRUUlRWeVZtMUJNVmRHV2toTldHZFlaVVp6TVZWWGQzcFdiMXAyWmtaQ1YxSXpUalJaTW1Ga1YxWnpSMVJ3YTA1bFJYTlRWbTVtWVUxSFRXRlViMnRXWkRKcmRGVnZWVEZXVmxwMlZXNW5UbFp2YnpWWk1GWkxWREZhZDA5VVRsZGxXRkY2VmpKMllXWXlUa1pYYjFwT1VtOXVlbGRVUm01VU1sSllVMjVhVDFZelVsaFdjREV6VFZaYVdHaEhkMDVTYm5Nd1ZuQTFWMVV5UldKa1JsSmFWak5TVEZWalJucFhSMUpIVkc5V1UyUXpRbGxXYm1jd1pqSktSMU51V2xoa00xSlhXVzlyVTJadldYcFdWRVp0WlZWelIxbHVaekJXTURGV1prVnZWMVl6UWtSVmJVWmtVakZTZFdWSGMxTldjVUpqVjFjeE1HY3hXblprTTJ0WFpESlNWVlJXV25wVFJscElhRWhPVmsxV2MxcFdWM2R1VmpKRllWZHhjMVpOVjFKWVZtMUtSMU5YU2tkVmIyZHNWbTVXTTFadldtUldNa2w2VGxWclUyVnVjMnRWYjJ0RFZsWmFkMmhJWjA5U2NVSlhWbkExVDFaR1duVm1Sbk5ZWkRGYVRGWlVRV0ZTTVVwMFZHOWFUbFl4U2tsWGJtYzBXVlphZGxkeFJsTmxSVFZ6VlhCaGVtaEdXbFZUYlVKUFVtNDFXRmxVVG01WlZrcFpVVzlXVmsxSFVUQldNVnBYWm05YWQwOVdTbXhTY1VKSVZtMUtNR1l4V2tkVFdITldaRzlhV0ZadVZtUm1iMWw2VjI0NWJVMVZOV0paTUZwdVZqRmFkV1pGWVZkV2IzTjBWRlphVDJZeFduaFViMVpyVFRGS1ZWZFhNREZSTURWSFprWmFXbWh2V2xCV2NERXdUVEZuZFdSSFJsZGxWVmt5Vlc5cmNsWndTbGxrUm10V1pWaE9ORlZ3WVc1bWNFNUhXa1UxYTAwd1NrVldiMUpEWkRGUllsSnZaMVZsUmxwVldWaHpWMlp2V25aVmJrNVBaVWRTVmxWWE5XNWxSbHAxVGxWeldtUXhjMFJXVkVaTFYwZEdSazlXWjA1V2IzTXhWMjVTUjJkd1ZrZFZjVlpYWlVaemNsUlhOVkpvYjFwWWFFZEdWRTFFUmxoWmJtdExWMGRGWTJSSVRsZGxXR3N6Vkc5YWVsWXlSa1phUm5OWFpETkNObFpYTVhwV01WcDJWMjluV0dRemEydFZjR0Y2Wm05elZsZHZaMjVTYjBwaldUQmFVMVV3TVVkbVJXdFhaVWRSZWxkV1ZURlNNVnAwVjI5V2EwMXZTbGxXVjNOQ1RWZE9SMVpZYTFaa01EVlZWbTFDWkUxR1VuWlhiMDVXWlVaelkxWXlNWEpXTVZwMlprWkNWbWh1V2xCYVJtZExVbTluZDFKd2EwNWxjR3RNVmpKM1pGbFhSV0ZVV0d0c1VtOXpUMVZ1Vmt0bVJtOVZVMjFTVWsxV1NsZFdjR0Z1VmtaS2RtWklhMVpsV0ZGNlZuQXhSMDV2U25abFJtZFRaVWhDVVZaWE1HRlRNazUyWlROelpGSnZjMDlWTUZaTFUwWmFXR1pGWjFWTlZuTklWa2RoVjFWd1NsbFJjR3RXWlVkU1VGUnVXbVJTTVZaMldrWk9UbEpGV1hwWGJsWlhUa1phU0ZOeFZsSldSVnBZVlc1V1MxWXhjMFZTY1VwdlpWVTFSMWx1VlRGVk1VbGpaRVp6VjFaalJUQlZNakZYVWpGbmVGWnZVbXROY1d0aFZuQmhVMll4VFdGbVJscHJVbkJTY2xsdVZucFNNVzkxVm5GblZVMVdjMWhXY0hOUFZsVXhXRlZ2VWxabFdHdFlXa1puUzFORk1WZFZiMnRUVFhCUlkxWXhXbE5STVZsaFZIRlNWbVZIWVZoWlZFNURWakZTVlZGd1JtNWxSbHBqV1ZWbU5WUnZXWHBYY1c5YVZrVTFkVlp1V2xwbk1XZDFaVVphVGxZeWF6WldjSE5MVkRGbldGSnVaMVpsUmtwVVZuQmhkV2hHV2xkWGIxcFBWbTQxWTFsdVduWmtWa2xpYUVaV1YyUXhXak5XUkVaa1ptOW5lRnBHV2s1U1JWcFlWa1phVjFsV1VuWlhiMmRZWlc5S1YxUldXa3RUUm05WWFFaEtiazFXV21KWmJscDZWRzlaWWxvemExZGxSa3BEV2tSS1VtaEdUbGxhUjBaVFpEQnpVVmRXVWtkWGJqRjJWMjlXVTJWSFVsUldjSFpoVG05V2QyaEhkMnRXTUhOSVZqSTFSMVl3TVZkWGIyZGtWbFp6WkZwWE1VZFNiMXAyVlc5blRsTkZTVEJXTVdaaFRrWlJlazFXWjFoa01YTlpXVlJPVTFaR1duWmFSemxUVFZoQ1dWUnZWbTVrUmtsNlRsWnpXbFpXV210V2JVcExabTlPZGxadldsZGxWMnRaVmxkelIxbFdaMGRWY1U1clVtNDFjbFJYWVV0V2IxcDJWVzVPVmsxVk5WaFdWMkZrWkZaT1IxZHZaMXBsV0d0clZtOWFkbWRGTlZsYVJUVlhaRE5CWVZaWE1ERlZNVloyVjI5clZtUXlVbXRXYlU1eVZVWlpZbWhHVGxkTlZrcGlWakpoWkZSdlowWlRiMmRZWkRGemExcEVSa3RuUmxwMldrWldhMDB5YTFaV2NIZFhVekpXUjJWR2EyNVNNRnBWVlhCaFMxZEdXa2huU0U1WFVtNDFTVnBWVm5aV2NFWjFWMjVoV21WWWEwdGFSRVo2VW5CS1NHWkdaMnhUUlVZMFZuQmhVMVF4U1dKVmIyZFZaREpoYTFWd1lVdFhSbEpWVVhGblZFMVdXbU5YYm10dVpVWktkbVpGYTFkU1kwWjVXVlpuUzFKd1RrWlViMmRyVFZaek1sWlVSbFpPVmxwMVQxWmFUbFp2U25OWlZFWjZVa1phVlZKd09XeE5ialZpVkZaclMxWndSV05SYjFwWFpYRkNXRlJXV25wWFJUVlhXa1pyVTJRelFsaFhWRUpUVWpGYWRVMVZhMVZrYmpWWVZXOW5VMDB4Vm5SU2JqbFlWakJ6U0ZaWFlVOWtWa3AyWmtoclYxZElRbEJWWTBaV2FGWldkVlp2V214bFYydFlWMVpTUzAwd01YWldXR2RXWkdOdlZGbHVXblpOTVZsaWFFVTViRkp2YzFwVlYzWXhWbTR4U0ZWdlFsZFdWbk5RVm0xR1QyWldTblptUlRWVFpETkNURlp1V21SWlZsRmhaVVpuV0dReWEzUlVWRXBUVmtaYWQyZElXbTVOVjJGV1ZWYzFUMVF4U25WT1ZtdGFWbGRyZFZadFJtUldNV2QwVW05YVRsWnhRazFXY0hka1ZERmFkbGR4U201U2IxcFlWbTVuTTAxR1duZG5SMFpWVFZWdk5WWkhOVmRrVmtwVlZtOXJWVlp3YTBSVk1tRlRWakZhVlZadlVrNWxSbk5ZVjFkM2JtWXhXa2hUYjFwWVZrVmFXRmxYZDB0b2IzTkdWMjQ1V0ZadmMySlhibHBrWkVkRllXWkdRbGRXTTJ0VVZWUkJNVll5U2tsVGNFWk9UVzlLVjFad1lXNWxNVXAyVm0xYVUyUmpiMWhaYmxaNmFGWnZWbFp4VGxWbFJuTllWakZTUTFkSFJuVlRjVXBXVFhGT05GVXhaMGRUVms1MlZHOU9WMDB5YTFGV2NEQjZaekF4Vms1WVRsUmxSMnR5Vlc5YWVsWkdVbGRXVkVaWVZtOWFNVmt3Vms5VWIxcDNhRVpyV2sxR1dtTlpWRVprWmpKT1NHUkdXazVsYjBwWlZtNWFaRlV4U25kU2JsWlRaVVp6VDFsWE1XTm5NVnAxVjNCM1UwMVdTbU5XY0dGa1pGWktSbGR2VWxwa01YTnJXVEZhWkZJeFduWmFSbEpYVFVSV1dWWnVaekJXTVZwSFUyOVdVMlF5YTFoVmNHRjZWVEZTVjFaVVJsZGxSMUpqVm5CaFQxVXhTbGRtUld0WVZqTnJWMVJ2V21SU01WSjJWbTlLYkdReGMzcFdWMkZ1WkRBMVIxZHVaMVpsUlRWVVZGWmFaRTFXYjNWWGNXZFdUVzV6TVZWWGMxTlpWbHBYVjNGdlpGSkZXbFJWTUdkUFUxZEtTR2hHWjFkTk1tdGFWbkJ6UzAxSFRXSldibXRVWlVaeldGbFhZV1JYUm05MlpFWk9VazFXV1RKV1J6VlBWakpLUm1WalNsZFNNMUpyV1ZablMxTldSblZvUm5OWFVsWnpVVlpYTUdGV01VNVlVMjVyVGxZelFsaFpWRWswYUVaYVdFMVVVbTVOVlRWSVZrZGhibFpYU25aWGIxWlhaVlJXUkZwV1dsZG1NVnAzWjBaV1RtUXhXV05YVjNkWFpqSkdkbE5ZYzFaa1kyOVlWbTFPY2xWR1VsZFhiamxYWlZVMVJsVndZV1JXTVZwMlprVXhXRlpGV25WWFZscFBabTR4Vm1SSGMxUlNWbk5oVmxkM1ZrMVdVV0ZYY1VwWFpWVmFWMVJWVWtkV01XOVdWbkJHYkZKdmMxZFdiMnR5VjI0eFYxZHhXbFpOY1d0aldUSmhlV2h2YzBobVJtZHNWakpyVFZadlVrZFpWMFZpVlc1clZXVnVjM0pWYmxwa1ZtOVNWbHBFVWxkU2IzTklWakl3TlZVeFduVk9WVnBXWlZocldGWnVXbVJtYjJkMlZtOWFhMlF3YzNKV1ZFSmtWVEpTU0ZWdVdtNVNiMHBQVkZjMWNsZFdaMVZTY0VaVlRWVTFZMVl5TlZOVU1WcEhVMjlTVjJReFdreFZiVVpXYUZVMVdWUnZVbE5rTTBKSVYxWldVMVV5UmxkVGIxcFlaRE5TYTFWd1lYcE5NV2RYV2taS2JrMXVjMGRaYmxwVFpGZEtkVk5VUWxkbFdFSlFWVlJHVm1oR1VuWmtSbHByYUc5YVdWWndZV1JaVmxwSFYxaHZiVkpYVWxOWmJscDZVMjlWWW1aR1oxWk5WbTgyVlZkM01GWnVNVWhrU0hOWFRVZFNVRnBHWjBkVFYwWkhXa1puVjJWdVNrMVdjSGRrVlRGRllWTllhMVZrTW10clZXOW5VMlpXV25aYVJ6bFBVbTl6TUZwRlZqQldSMHBIWlVSYVYyVllVak5XYm1kTFpqRm5WVkZ2YzA1bGIwb3lWMjlXWkZOd1VXRldiMjlrVWpOcldGWndOVU5UYjFwVlVtOWFiMUl4U2xoV1IyRnVWakpLUmxOdU9WWmxSbk5rVkZaYVZtaEdXbmRuUmxKWFpHTkZNbFp3TUdGTlIwWllVMjVuVkdSamIxaFVWVnBrWjFaelYxcEZXbTVOYjFwSFYyNWFUMVJ2V2xWUmJWWllWa1ZhVkZWVVJsTm1Na3BKVTI5YWEwMHhTbEZXY0RGalRWWlJZVlZ2YTA5V2NGSlZWWEIzZGs1R1dsaE5XR2RXWkdOR1JsVndZVk5YYmpGWFpraEtaRlp3VWxoV01GcFRaakZhZGxWdlRsZE5NbXRrVm01YWJrMUdXV0ZVV0c5VlpVZHJWVmx3TVhKV01XOTJWbFJHV0ZKdldtRlZWelZQVmtkS1IyWkdhMXBOUm5OVVZsZGhXbWh3UmtaYVIwWlhaVVp6TmxaSGQyNVRjRlozVW01YWJGSXlhM0phVjNka1ZqRmFTR2hIYzA1V2IwcGlWRlpXY21ReFRrZFRiMUpYVFVkU2VGUldXbnBXYjFwNFdrWm5WMlZHV1RCV2JVb3daakZTZDFKdFdsTmxSbk5YV1c5clExUkdWblpXV0d0WFpWWmFSMWx1WjBkVWIwcDRVVlJDVjFkSVFsQlpZMFp1VTBaU2VGVnZUbXhsVjJ0WlZsZGhiazVHV1dGWGJsWlVaVzQxVkZsdVZURlRWbWQxV1ROclYxSnVjMGRaTUZwWFZqSktXVlZ3YTFaTmNXdFVWbTFLVDFOR1NuWmFSbEpUWlVoQ1UxWnZaelJsTWsxaFUzRlNVMlZ1YzFsV01HZFRabFphZDJoSFJsUldjR0ZqVm5CaGJtUXhXblZtU0d0V1pWUkdTRlpIWVV0WFYwWkdaa1pyYTJRelFrMVdWRW8wVmpKU1YxZHhVbXRTTW1GelZXOWFlbFZHV2toblJscHVUVzlhV0ZVeVlYWmtiMDVJYUVaclZrMUdXbXRWVkVaWFowZFdSMVJ2WjFObFZrcFlWa1phWkZVeFZXRlhjVTVVWkc1YWExWndZV1JUUmxsaWFFVjNWMlZWV2tsWk1GcFBWRzlLZFdaRk1WZGxSa3BJV1dOR1QxWXlTa2RYYjJkc1VtOXpWVlp3ZDFkWlZUVkhWbGhuVjJWSFVsQldjSFl4VjFaVlltZEhPVmRTYm5OWldsVm1OVmR1TVhSV2NWcGFaVmhyYTFadFNrOVNNVloyVTI5bmJGSlhPR0ZXTW1GWFpUSk5ZVnBGWjFWbFIyRnpWVzFPUTFaR1VsVlJjVnBPVW5CU1lWVndNRFZXVjBZMlVXMU9WVTFYYTFSWlZ6RkxVbkJKWTJSR1oydGtNSEpqVm05U1IxVXhXV0ZhU0VwVlpVWktUMVp2VWxab1JscFZVbkJHVkUxV2MwaFdSMkZrVmpKR2RsTnhSbGRsUmxWaFZWUkdWbWN5UmtoUFYzTlhaVVZ6UjFadVp6QlRNa1pZVWxoclYyUnVOVlpVVmxwa2FHOVdkMDFXWjI1V2JuTmpWbGN4ZGxSdU1YZGtSa0pYWlZoQ1JGa3lNVmRXTVZaMlpVWm5hMDF4YTJ0V2NHRmtXVlpTZGxaeFNsZGxWRzlRVm5CaFIwNXZWbGRrUnpsWVpHTkdZbFl5YzBkV01WbzJVbGhuVjJReVVreFpZMFpQWm5CT1JrNVdUbGRsYmtwTFZuQjNVMUV5UldGVWNVcE9WbGRyZEZVd1ZtUm1WbTkzVFZjNVYxWnZjMkpXY0RWUFZrVXhkbE52YTFwTlJscHJWa2RoU21oV1ZuaFZiMXBYWlVaek1sZFdaelJUTWxKR1QxWm5WR1ZHV2xoWldITlhVMVpuZGxad1JsVk5Wa3BJVlRKaGRsbFdTblZUY0VaYVZrVnlNRlp1V2xab1JtZDNVbTlXYkZKdmNucFdNbmRrWmpGYVIxUnVhMVpsUmxwWFZGYzFVMDB4VW5WYVJtZFlWakJhU2xsVldsTldSa3AyWmtoclYxWXpVbGhaWTBaUFpqRmFXV1ZGT1ZkWFJVcFVWbkExZWxZd05VZFZiMnRQVmxaelQxbHVWVEZvYjFWaVRsYzVWMDFFUmtsV1YzWmhWMjR4VjJaSGEyUlNjRkpZVlhCaFpGZFdjMGRVYjJkWVVsVnpORlp0Um01TlIwbGlVbTVyVldReWEzUlZNRnBrVmpGdldXWkZTbTlTYjFvd1ZHOXJUMVZ3U2taT1dHOWFUVVpLV0ZaWFlXUldWMHBGVkc5YVRsSnZXVEJXVkVvMFZURlpZVlp2VmxOa1kyOVVWbkExUTFaV1drZFhiMmRQVW01elkxWndOVmRXTWtwMVYyOVNWbVZIVVRCWk1WcFdhRVphV1dSR1oxZFdSMkZYVm05blkwMVdVblZOV0VwUFZqQmFWMWx2YTFObWIxcEZVMjVhYmsxWFVtSmFWV2MwVmpKS1YxTlVSbGROVm5OWVZuQjJZVkl4VG5oVWIwNXJUVmhDVUZaWFlXUlpWazVYVjI5V1UyVllVbFZXY0RFMFYyOWFkMmhIZDFaTmJsWTFXbFZXTUZZeVJXRlhiMmRrVWtWYVVGWndNVWRTYjJkM2FFWm5iRlp1Y3pOV2IyWjZUVmRKWVZSeFRtUlNjR3RSVm5CaGVsWkdXblZYY1dkVVVtOXpXVlJXVWtOa01VcDFaa1p6V2xaWFRXRldNakZMWm05T2RXWkdaMU5sVmtwSlZsZHpSMWxXV25aWGNVNVhaVVpLV0ZZd1ZrdFNNVnBIVjI5blYyVldXa2hXTVd0eVYwZEtkMlJHVmxabFJrcElWakJhVm1jeFZuVlBWMkZUWlVoQ1NWZFhjMDlrTWtwSFYzRlNiMUpYVWxkWlYzZEdUVlpTZFZkdVoxZGxWWE5KV1c1bmNtUldUa1pUYmpGWFZqTnJWRlp0Umtwbk1ERlpWWEJ6VGsxdlNsVlhWM2RYWjNCUllWVnhUbGRsV0VKMldXOWFaRmRHWjNWV2NXZFZaVlZhWTFZeGEzSldjRXBaVVc1clYwMUdWalJaTW1Ga1pqRlNkMmhHWjFkU00ydElWbTlTUTFZd05VaFZibWRWWkRGYVUxbFVRbnBWUmxwMlYzRmFiMlZHYzFaVlYzWTFWVEpLUm1WRVRsVmxSMnRNVm01YWJsTldSblpXYjJkT1VtOXpNVmR2Vm1SWGNGWkhWbkZLWkZKdmMzTlpiMnR5VjFaYVdFMUVSbTVOYjFwSlZsWnJlbFZ2WjBsUmNVcFhaVVp6TTFVd1dtUm1NVnA0Vkc5blUyUXpRbGRXVm1jMFZUSkdSazFWYjFKV1JWcFlXVmQzZWxSR1ZsaE5WbWRVVW05S01GbFZaM3BWTWtWalVXMUdWMlZZUWtoYVJFWk9hRlpLV1dSR1dtdE5NVXBqVmxSQ1pGWXdNR0ZXV0d0WVpVVTFXRlZ3ZGpGWFZsSjJWM0JHYTJWR2MwaFdNbmQ2V1ZaWlkxVnZhMVZsV0d0VVZYQXhUMUpXVm5WT1ZtZFhUVEpPTkZadFJsTlNNa1ZpVm05clYyUXlVbFpaYm1keVZsWlZlbVJGU205U2NVSlhWbkJoYmxaRk1WaG5SRlpYVFhGU1kxWkhkbUZtYmpWWFpFWmFhMlF3YzJKV1Z6RmpUVmRPZDFOdVoxaGxSVFZZVkZSS2NsTkdaM1pXY0RsWFRWVTFTRlV5ZDFkVmNFVmpVWEZPV2xaRmNucFVibHAxYUVabmQyZEdjMWRXUlZwWlYxUkNjbFV4VldGWGJWcFRaVVZhVjFsWGQwdE5NVnBWVW05T1ZGSXdOVXBXY0dGa1ZqRmFkbVpHV2xka2JuSXdWbTFHVjFJeFRsbGFSbXRzVWxoQ1dGWkdaelJuTVUxaFprWm5aRkpVYjFWV2JVRXhVMFphU0dkRmQydFdNRmt5VlZkelYxbFdTblptUld0V1pWaHJVRlp0Um5wU1ZsWjJVMjluVjAxd2FqRldjREJoVFVkRllWUnZaMVZsUjFKWVdXOVdaRlpXVWxobU0ydFBaVVpXTlZSdmEwOVhSa3AzYUVSQ1ZVMVdTbFJXYmxwa1pqSk9SVlp3UmxkV01tdEpWbTFDYmxNeVVsZG1SRnBXWkdOV1ZGWndZWFZuTVZsaVRsaG5XbFp1TldOV1IzZGtWRzlaWTFGeFJscGxWRVo1Vkc1YVpHWXhXblpYY0dGVFpERnpXRlp1WnpCa01WVjZUVlZXYkZKVk5WZFVWelZ5VjBaU2RsZHZjMjlsUlRVd1dWVmFUMVl5U2tsUmNEbFlaVVp6ZVZWdFNrcG9WbEo0Vkc5YWJHVlhhMk5XVnpWNlZtNHhSMVp4VGxobFdGSjFXVzVhWkZZeGIzVlhiamxXVFc1elYxWXlOVWRXTVVwWFYxUkNWazF4YTB4V2NERlRVMVpuZDJoR1VsTldjVUpKVm05bU1XY3hVV0ZTY1VwT1UwZHJkRlZ3WVhwWlZsSldaRWM1VlZKeFFsZFpWV3RQVjBaS2RXWkZaMXBXVmxWaFZtNWFUMUp2VG5aWGIxWnNVbkZDVVZaWGMwSm9SMUpJVlc1YWExSXpRbk5aYjJkdVRrWmFWMWR2WjFOTlZuTllWbTlyY2xkSFJXSmtSbFpWVm05VllWWndZV1JTTVc1alpFWm5VMlZXU2t0V1ZFb3daekZhZFUxVmExWmtNbUZXVm05YVpGZEdXV0pvUlRsVFZtNWFNVmxWV21Sa1JURlpVVzlTV0dWR2MxUldSRVpMWjBaV1dWcEdUbXROY0d0VlYxWm5NRk14VFdGYVJtZFhWMGRyV0Zad01UQk9SbGxpVFZWblYxSXdjMWxXUjNOUFZuQktSMlpGWVZWbFJuTXpXVEl4UzFJeFduWlhialZUVFRKclVWWnVXbE5SY0ZaSFYzRk9WV1F4YzNKVmNHRkxWa1pTVm1SSE9WVlNjVUpYVmxkM2JsWkhSalpTYm1kYVpERnphMVpVUmt0WFIxWkZWVzluYTJRd2N6RlhibEpIVm5CV1YxZHhTbGhsUmtwVVZGZGhTMmN4V2xWUmNIZFRUVzlHTlZWd05VdFhSMHBIWmtaT1YyUXhjMnRWTUZwWFRtOU9kVTlXVW14U1dFSmtWMVpXYlUxV1dXSlRjVXBUWkc0MVYxUldaMU5UUm5ORlVuQkdWMlZGYzFwWk1GcFhWakZLVmxkWWMxZFNjRkY2Vm0xR1QyWXhXbGxrUjBaVVVqRktWbFp3YzBKTlZrNUhWMjVuV0dWRmMzWlZiMUpYVWpGU1ZtUklUbFpsUm5OSFZUSjNORmxXV25abVIydGFUWEZyVEZZeFowdFRSMDVIV2tVMVUxSldjMWRXYjJjMFdWWlJZV1ZHWjFWWFIyRldXVzlyVTFaR1duWmtSVXB2VW05Wk1sVlhOVXRrTURGMlYyOXJWMDF0Vm1OV2JsVmhVbTluZFZSdlowNWxiMFl6VjFabk5GVndVV0ZYY1VaWVpVaENUMWxVVGtOVGIxcFpaa1U1YlUxV2J6UldWMkZ1VlRKS1IxTnZaMXBXUlZvelZtNWFVMVp2Vm5WVWIxSlRaVVp6V1ZadVdsTlRNa1oyVTI5cmExSlViMWhaYjJ0VFpFWlZZVmR2VGxkTlZuTmlWMjVhYmxZeFdraGFNM05YVmpOQ1JGbGpSbTVTTWs1SlZIQnZUazF2U21GV1YzTlBVVEF3WVZkdlZsSmtNbEoxVm5CMk1WWXhibnBWYm1kc1VtNXpXRll5ZDNaV01VcEdaa2RyVmsxR1ZqUlZNV2RMVTBkS1NHVkZOVmRXUmxWNlZuQnpRMlJ1TVZkVVdHOVRWMGRTV1ZsWWMwZFdWbHAyV2tSU2JWSnZWalZhUldZMVZrZEtSMlZFVGxwa01tdFVWbTVhWkdadU5WWmtSbWRzVWpGS1RWZHVWbVJWTVVwM1UyNW5WV1ZYYTNKVVZWSlhVakZhVmxkdlNtNU5WVXBUVlVaUmVsQlJQVDA9'
    decode(x)