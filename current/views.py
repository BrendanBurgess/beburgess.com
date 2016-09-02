from django.shortcuts import render

mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]

mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]

#random mobile dector I found online
def mobileBrowser(request):
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser


# Create your views here.
def index(request):
	page = 'current/index.html'

	if mobileBrowser(request):
		page = 'current/m_index.html'

	context_dict = {}
	return render(request, page, context_dict)

def about(request):
	context_dict = {}
	return render(request, 'current/about.html', context_dict)

def projects(request):
	context_dict = {}
	return render(request, 'current/projects.html', context_dict)

def interests(request):
	context_dict = {}
	return render(request, 'current/interests.html', context_dict)

def poli(request):
	context_dict = {}
	return render(request, 'current/poli.html', context_dict)

def comp(request):
	context_dict = {}
	return render(request, 'current/comp.html', context_dict)

def contact(request):
	context_dict = {}
	return render(request, 'current/contact.html', context_dict)