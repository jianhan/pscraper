# import libraries
from bs4 import BeautifulSoup
import requests


def scrapeNcix():
    # start with ncix
    ncix = "https://www.ncix.com/categories/"

    ncixRsp = requests.get(ncix, timeout=5)
    pageContent = BeautifulSoup(ncixRsp.content, 'html.parser')
    subCategories = pageContent.find_all(class_='sub_link', href=True)
    for s in subCategories:
        print(s.string,s['href'])
        subCat = requests.get(s['href'], timeout=5)
        subCatContent = BeautifulSoup(subCat.content, 'html.parser')
        listing = subCatContent.select("span.listing")
        print(listing)
        break

def scrapNcixListing(url):
    pageContent = """
    

	
	
	

	
	




	



		
		
		



	
		
		
	








	



























	








	









	


	



















 


	 	





   

















	
	
	























	
	
		
	




  




	












		

  







  













	
	
	
	
	
	

	
	
	
	
	

	

	


















		
		




	
































	
		
<!DOCTYPE HTML>
<html lang="en">

<head>



<meta http-equiv="Content-language" content="en">
<meta name="msvalidate.01" content="0B92FCDD6A64C511CFD1C8D4105272C3" />





 
	
	

	
	
	

	
	
	
	
	
	
	
	
	
	
	



  



 
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
















	
	<title>Computer Memory, DDR3 Memory, RAM, Desktop Memory - NCIX</title>
	<meta name="description" content="Shop our selection of DDR3 Ram / Memory from top manufacturers such as Kingston, G.Skill, and Corsair
computer cases for ATX, mATX, mITX. Top models from Antec, Corsair, Fractal Design, In-Win, NZXT, Phanteks, Cooler Master">
	<meta name="keywords" content="DDR3 memory, discount computer memory in Canada, buy DDR3 SODIMM, buy computer memory">
	<meta name="robots" content="all">
	<meta property="og:site_name " content="NCIX" />
	
	


<link rel="shortcut icon" href="/_img/favicon.ico">
<script type="text/javascript" src="/js/jquery.min.js"></script>
<script type="text/javascript" src="/js/jquery-ui-1.8.2.custom.min.js"></script>
<script type="text/javascript" src="/js/jquery.cycle.all.min.js"></script>
<script type="text/javascript" src="/js/ncix.js?v=20171017"></script>
<link  rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:400,300,700">
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400' rel='stylesheet' type='text/css'>






	


	
	
		
		
			
				 
			
			
		
	

 


	<link rel="canonical" href="https://www.ncix.com/category/ddr3-memory-d0-1303.htm" />



<link rel="stylesheet" href="/css/ncix.min.201711091.css" type="text/css">

	<script>(function() {
	
	  var _fbq = window._fbq || (window._fbq = []);
	
	  if (!_fbq.loaded) {
	
		var fbds = document.createElement('script');
	
		fbds.async = true;
	
		fbds.src = '//connect.facebook.net/en_US/fbds.js';
	
		var s = document.getElementsByTagName('script')[0];
	
		s.parentNode.insertBefore(fbds, s);
	
		_fbq.loaded = true;
	
	  }
	
	  _fbq.push(['addPixelId', '539410282848532']);
	
	})();
	
	window._fbq = window._fbq || [];
	
	window._fbq.push(['track', 'PixelInitialized', {}]);
	
	</script>
	
	<noscript><img height="1" width="1" alt="" style="display:none" src="https://www.facebook.com/tr?id=539410282848532&amp;ev=NoScript" /></noscript>
	
	
	
	
	
	<script>
	  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	  ga('create', 'UA-25458666-2', 'auto');
	  ga('require', 'displayfeatures');
	  ga('send', 'pageview');
	
	</script>
	

<script>(function(w,d,t,r,u){var f,n,i;w[u]=w[u]||[],f=function(){var o={ti:"4004102"};o.q=w[u],w[u]=new UET(o),w[u].push("pageLoad")},n=d.createElement(t),n.src=r,n.async=1,n.onload=n.onreadystatechange=function(){var s=this.readyState;s&&s!=="loaded"&&s!=="complete"||(f(),n.onload=n.onreadystatechange=null)},i=d.getElementsByTagName(t)[0],i.parentNode.insertBefore(n,i)})(window,document,"script","//bat.bing.com/bat.js","uetq");</script><noscript><img src="//bat.bing.com/action/0?ti=4004102&Ver=2" height="0" width="0" style="display:none; visibility: hidden;" /></noscript>




<!-- Facebook Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window,document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '539410282848532'); 
fbq('track', 'PageView');

</script>
<noscript>
 <img height="1" width="1" src="https://www.facebook.com/tr?id=539410282848532&ev=PageView&noscript=1"/>
</noscript>
<!-- End Facebook Pixel Code -->

</head>
<body leftmargin="0" topmargin="0" marginheight="0" marginwidth="0" >










<table width="100%" cellpadding="0" cellspacing="0" border="0">
		<tr>
		<td>
	<table width="100%" cellpadding="0" cellspacing="0" border="0">
		<tr>
			<td width="180" valign="bottom" >	
				<table style="padding-top:0px;" cellpadding="0" cellspacing="0">
					<tr>
						
						<td  id="mainlogo" style="margin-bottom:0px; padding-bottom:0px; padding-left: 3px; padding-top:1px;  " valign="bottom">
							<a href="https://www.ncix.com"><img src="https://dhsj95t7aazhx.cloudfront.net/logo/NCIX-dotcom-logo.gif" border="0"  title="NCIX.com Canada - Computer Hardware, Laptops and Electronics!" alt="NCIX.com Canada - Computer Hardware, Laptops and Electronics!" /></a>
						</td>
					</tr>
				</table>
			</td>
			<td valign="top">
				<table width="100%" cellpadding="0" cellspacing="0" border="0">
					<tr>
					
						<td align="right" style="padding-right:10px;">
								<table width="100%" cellpadding="0" cellspacing="0" align="right">
											<tr>
												<td>
													<nav id="primary_nav_wrap">
													<ul>
													<li id="loginstatus1">
													<a href='https://secure1.ncix.com/login/' style='color:black'  rel="nofollow"><span class='signinbtn'>Sign up</span></a>
													</li>
													
													<li style="margin-left:15px;"><span id="loginstatus2"><a href="https://secure1.ncix.com/login/" rel="nofollow">Sign in</a></span>   &nbsp;<font color="#999999">&or;</font>
													<ul>
													<li id="loginstatus3" style="display:none"><a href="https://secure1.ncix.com/login/signout.php">Sign out</a></li>
													<li><a href="https://secure1.ncix.com/account/"  rel="nofollow">My Account</a></li>
													<li><a href="https://secure1.ncix.com/ordertracking/"  rel="nofollow">Order Tracking</a></li>
													<li><a href="https://secure1.ncix.com/wishlist/"  rel="nofollow">Wish List</a></li>
													<li><a href="https://secure1.ncix.com/cart/?mode=savedcarts"  rel="nofollow">Your Saved Cart</a></li>
													</ul>
													</li>
													
													<li>
													Shop by &nbsp; <font color="#999999">&or;</font>
													<ul>
													<li><a href="https://www.ncix.com/categories/">Category</a></li>
													<li><a href="https://www.ncix.com/brand-store/">Brand</a> </li>
													<li><a href="https://www.ncix.com/promotion">SALE</a></li>
													<li><a href="https://www.ncix.com/openbox/">Openbox</a></li>
													<li><a href="https://www.ncix.com/clearance/">Clearance</a></li>
													<!--
													<li><a href="http://secure1.ncix.com/affiliate/">Coupons</a></li>
													-->
													<li><a href="https://www.ncix.com/supershippingsaverclub">Free Shipping</a></li>
													<li><a href="https://www.ncix.com/coupons/">Coupon</a></li>
													<li><a href="https://www.ncix.com/new/">New Products</a></li>
													</ul>
													</li>
													
													<li>Contact us &nbsp; <font color="#999999">&or;</font>
													<ul>
													<li><a href="https://www.ncix.com/contact/">Locations</a></li>
													<li><a href="https://www.ncix.com/article/customercare.htm">Customer Care</a></li>
													<li><a href="https://secure1.ncix.com/message/"  rel="nofollow">Message us</a></li>
													
													</ul>
													</li>
													
													
													<li>Mobile Apps &nbsp; <font color="#999999">&or;</font>
													<ul>
													<li><a href="https://tinyurl.com/a49ngav"  rel="nofollow"  target="_blank">iOS App</a></li>
													<li><a href="https://play.google.com/store/apps/details?id=com.ncix.app.android"  rel="nofollow" target="_blank">Android App</a></li>
													<li><a href="https://bit.ly/1guO0Pn"  target="_blank"  rel="nofollow">Windows App</a></li>
													<li><a href="https://m.ncix.com/"  target="_blank"  rel="nofollow">Mobile Site</a></li>
													</ul>
													</li>


	
													</ul>
													</nav>
												</td>
											</tr>
										</table>
						</td>
						
					</tr>
					<tr><td height="10"></td></tr>
					<tr>
						<td>
							<table width="100%" border="0" cellspacing="0" cellpadding="0">
								<tr>
									<td width="100%" align="center" style="padding-bottom:1px">
										<div id="search_container" style="position:relative; width:480px; border-radius:4px; border:1px #969696 solid; margin-left:-30px;">
											<table border="0" width="100%">
												<tr>
													<td align="left">
														<table border="0" width="480">
															<tr>
																<td nowrap="nowrap">
																	
																	<form name="quicksearchform_a" action="https://www.ncix.com/search/" method="GET" style="margin:0;padding:0;">
																	<table border="0" cellpadding="0" cellspacing="0" width="100%">
																		<tr>
																		
																			<td style="padding-left:3px" width="80%">
																				<input name="q" value="" style="border:1px;outline-style:none;padding-left:2px" onKeyUp="doSearch(this.value);" id="q" class="searchbar_style" autocomplete="off" align="middle" type="text" onClick="hotsearch()">
																			</td>
																			<td align="right" style="padding-right:6px">
																				<input src="/_img/search-btn.gif" name="imagefield" onClick="quicksearchform_a.submit();return false;" align="absmiddle" type="image" alt="Search" title="Search">
																			</td>
																		</tr>
																	</table>
																	</form>
																	<div id="jsonDisplayResult"></div>
																</td>
															</tr>
														</table>
													</td>
												</tr>
											</table>
											</div>	
								
									</td>
									<TD width="150" align="right" valign="bottom" style="padding-right:6px; padding-bottom:0px; margin-bottom:0px;"> 
										<div class="shopping_cart_item" alt="Shopping Cart" title="Shopping Cart"><A  href="https://secure1.ncix.com/cart/" rel="nofollow"><span id="cartcount"  style="color: #ffffff;font-weight:normal; font-size: 15px; height: 36px; line-height: 36px;">Cart</span></A></div>
										<SCRIPT language="javascript">
											var cartitem	=	getCookie("CARTITEM");
											if(cartitem > 0){
												$("#cartcount").html("Cart ("+cartitem+")");
											}
										</SCRIPT>
									</TD>
								</tr>
							</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	<!-- MENU BAR-->


	
<div id="wrapper">
		<nav id="nav"   style="width:1150px;">
			<ul style="margin-top: 9px">
				<li>
					<a href="#"  alt="Department" title="Department">Department</a>
					<div class="drop">
						<div class="drop-holder">
							<ul class="category-list">
								
								
									
									
									
										
									
									<li class="active">
										
										
										<a href="https://www.ncix.com/computer-hardware/">Computer Hardware</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/cpus-processors-0b-106.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/106.jpg?v=20161230" width="110" height="55"  title="CPUs / Processors" alt="CPUs / Processors">
															</div>
															<strong class="title">CPUs / Processors</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/computer-cases-53-104.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/104.jpg?v=20161230" width="110" height="55"  title="Computer Cases" alt="Computer Cases">
															</div>
															<strong class="title">Computer Cases</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/fans-cooling-50-1164.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1164.jpg?v=20161230" width="110" height="55"  title="Fans &amp; Cooling" alt="Fans &amp; Cooling">
															</div>
															<strong class="title">Fans & Cooling</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/hard-drives-d6-109.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/109.jpg?v=20161230" width="110" height="55"  title="Hard Drives" alt="Hard Drives">
															</div>
															<strong class="title">Hard Drives</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/keyboards-1b-101.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/101.jpg?v=20161230" width="110" height="55"  title="Keyboards" alt="Keyboards">
															</div>
															<strong class="title">Keyboards</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/motherboards-90-107.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/107.jpg?v=20161230" width="110" height="55"  title="Motherboards" alt="Motherboards">
															</div>
															<strong class="title">Motherboards</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/power-supplies-74-1066.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1066.jpg?v=20161230" width="110" height="55"  title="Power Supplies" alt="Power Supplies">
															</div>
															<strong class="title">Power Supplies</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/video-cards-72-108.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/108.jpg?v=20161230" width="110" height="55"  title="Video Cards" alt="Video Cards">
															</div>
															<strong class="title">Video Cards</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/2-5-hard-drives-b5-1044.htm">2.5" Hard Drives<span class="qty-count"> (62)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/adsl-cable-modems-b9-1039.htm">ADSL/Cable Modems<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/barbs-fittings-60-1289.htm">Barbs & Fittings<span class="qty-count"> (192)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/blu-ray-drives-e9-1263.htm">Blu-Ray Drives<span class="qty-count"> (12)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/bundle-deals-75-1265.htm">Bundle Deals<span class="qty-count"> (122)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cd-dvd-drives-bf-1015.htm">CD & DVD Drives<span class="qty-count"> (31)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cd-dvd-replicators-92-1338.htm">CD & DVD Replicators<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cpu-heatsinks-62-1023.htm">CPU Heatsinks<span class="qty-count"> (147)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cpu-water-blocks-74-1281.htm">CPU Water Blocks<span class="qty-count"> (32)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cpus-processors-0b-106.htm">CPUs / Processors<span class="qty-count"> (237)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/compact-flash-be-1308.htm">Compact Flash<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/computer-cases-53-104.htm">Computer Cases<span class="qty-count"> (462)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/coolant-additives-59-1285.htm">Coolant & Additives<span class="qty-count"> (21)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr-desktop-memory-6f-1297.htm">DDR Desktop Memory<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr-sodimm-7b-1298.htm">DDR SODIMM<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr-server-9f-1299.htm">DDR Server<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr2-desktop-memory-25-1300.htm">DDR2 Desktop Memory<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr2-sodimm-d9-1301.htm">DDR2 SODIMM<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr2-server-37-1302.htm">DDR2 Server<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr3-memory-d0-1303.htm">DDR3 Memory<span class="qty-count"> (126)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr3-sodimm-ram-19-1319.htm">DDR3 SODIMM RAM<span class="qty-count"> (58)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr3-server-ram-c7-1344.htm">DDR3 Server RAM<span class="qty-count"> (138)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr4-memory-27-1516.htm">DDR4 Memory<span class="qty-count"> (285)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr4-sodimm-ram-61-1517.htm">DDR4 SODIMM RAM<span class="qty-count"> (33)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ddr4-server-ram-21-1518.htm">DDR4 Server RAM<span class="qty-count"> (121)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/data-projectors-15-1228.htm">Data Projectors<span class="qty-count"> (106)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/desktop-sdram-f2-1304.htm">Desktop SDRAM<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/drive-enclosures-6b-1027.htm">Drive Enclosures<span class="qty-count"> (76)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/encryption-data-security-f8-1347.htm">Encryption & Data Security<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/external-drive-accessories-98-1359.htm">External Drive Accessories<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/external-hard-drives-ca-1272.htm">External Hard Drives<span class="qty-count"> (153)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/external-optical-drives-2d-1346.htm">External Optical Drives<span class="qty-count"> (11)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/external-ssd-85-1316.htm">External SSD<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/fans-cooling-50-1164.htm">Fans & Cooling<span class="qty-count"> (269)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/firewire-1394-cards-16-1048.htm">Firewire 1394 Cards<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/flash-card-readers-b8-1312.htm">Flash Card Readers<span class="qty-count"> (37)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/game-controllers-ab-1011.htm">Game Controllers<span class="qty-count"> (56)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/graphics-tablets-5c-1040.htm">Graphics Tablets<span class="qty-count"> (21)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/hard-drive-water-blocks-98-1291.htm">Hard Drive Water Blocks<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/hard-drives-d6-109.htm">Hard Drives<span class="qty-count"> (335)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/hose-clamps-e4-1293.htm">Hose Clamps<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/hybrid-hard-drives-ba-1361.htm">Hybrid Hard Drives<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ide-raid-cards-37-1047.htm">IDE/RAID Cards<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/keyboard-mouse-combo-c0-1345.htm">Keyboard & Mouse Combo<span class="qty-count"> (86)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/keyboards-1b-101.htm">Keyboards<span class="qty-count"> (352)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/macbook-flash-storage-77-1309.htm">MacBook Flash Storage<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/memory-water-blocks-04-1296.htm">Memory Water Blocks<span class="qty-count"> (14)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mice-35-102.htm">Mice<span class="qty-count"> (291)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/misc-5d-1286.htm">Misc.<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/modems-b6-1037.htm">Modems<span class="qty-count"> (5)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/motherboard-water-blocks-fd-1287.htm">Motherboard Water Blocks<span class="qty-count"> (62)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/motherboards-90-107.htm">Motherboards<span class="qty-count"> (429)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mounting-accessories-fb-1292.htm">Mounting Accessories<span class="qty-count"> (35)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-storage-nas-8c-1191.htm">Network Storage NAS<span class="qty-count"> (293)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-video-recorder-nvr-e4-1399.htm">Network Video Recorder (NVR)<span class="qty-count"> (42)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/pcmcia-modem-ba-1043.htm">PCMCIA MODEM<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/pen-scanners-da-1221.htm">Pen Scanners<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/portable-scanners-54-1423.htm">Portable Scanners<span class="qty-count"> (23)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/power-supplies-74-1066.htm">Power Supplies<span class="qty-count"> (291)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/projector-accessories-4a-1184.htm">Projector Accessories<span class="qty-count"> (26)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/projector-lamps-a7-1333.htm">Projector Lamps<span class="qty-count"> (65)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/projector-screens-24-1178.htm">Projector Screens<span class="qty-count"> (135)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/pumps-3e-1283.htm">Pumps<span class="qty-count"> (35)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/raid-cards-sas-59-1012.htm">RAID Cards - SAS<span class="qty-count"> (30)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/racing-wheels-75-1188.htm">Racing Wheels<span class="qty-count"> (22)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/rackmountable-b9-1328.htm">Rackmountable<span class="qty-count"> (29)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/radiators-shrouds-2d-1284.htm">Radiators & Shrouds<span class="qty-count"> (23)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/reservoirs-t-lines-a7-1288.htm">Reservoirs & T-lines<span class="qty-count"> (44)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/san-hard-drive-array-a6-1396.htm">SAN Hard Drive Array<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/sata-card-non-raid-f9-1458.htm">SATA Card Non-RAID<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/sata-raid-cards-6c-1215.htm">SATA RAID Cards<span class="qty-count"> (18)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/sd-secure-digital-c2-1310.htm">SD Secure Digital<span class="qty-count"> (88)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ssd-accessories-7d-1358.htm">SSD Accessories<span class="qty-count"> (22)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/scanners-11-1019.htm">Scanners<span class="qty-count"> (77)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/security-accessories-b2-1314.htm">Security Accessories<span class="qty-count"> (26)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/security-cameras-75-1315.htm">Security Cameras<span class="qty-count"> (217)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/serial-parallel-cards-ff-1097.htm">Serial / Parallel Cards<span class="qty-count"> (15)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/solid-state-drive-ssd-be-1275.htm">Solid State Drive - SSD<span class="qty-count"> (254)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/sound-cards-1c-1007.htm">Sound Cards<span class="qty-count"> (29)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/surveillance-hard-drive-d9-1329.htm">Surveillance Hard Drive<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/surveillance-systems-f9-1313.htm">Surveillance Systems<span class="qty-count"> (35)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/tv-video-67-1029.htm">TV & Video<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/tv-tuners-90-1271.htm">TV Tuners<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/tape-backup-drives-c8-1017.htm">Tape Backup Drives<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/tubing-7d-1280.htm">Tubing<span class="qty-count"> (19)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/usb-3-0-add-on-cards-76-1355.htm">USB 3.0 Add On Cards<span class="qty-count"> (9)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/usb-flash-drives-7f-1016.htm">USB Flash Drives<span class="qty-count"> (166)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/usb-video-card-54-1207.htm">USB Video Card<span class="qty-count"> (9)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/vga-water-blocks-c1-1279.htm">VGA Water Blocks<span class="qty-count"> (179)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/video-cards-72-108.htm">Video Cards<span class="qty-count"> (258)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/water-cooling-kits-80-1290.htm">Water Cooling Kits<span class="qty-count"> (28)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/webcams-45-1021.htm">Webcams<span class="qty-count"> (39)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/workstation-video-cards-64-1354.htm">Workstation Video Cards<span class="qty-count"> (58)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Computer Hardware-->
<a href="https://www.ncix.com/promotion/" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/ws/HolidayJumpstart2017-240w.jpg?3" border="0" display="block" alt="NCIX Weekly Sale"/></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/notebooks/">Laptop & Tablet</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/business-laptop-9e-1324.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1324.jpg?v=20161230" width="110" height="55"  title="Business Laptop" alt="Business Laptop">
															</div>
															<strong class="title">Business Laptop</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/business-ultrabook-53-1238.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1238.jpg?v=20161230" width="110" height="55"  title="Business Ultrabook" alt="Business Ultrabook">
															</div>
															<strong class="title">Business Ultrabook</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/chromebook-80-1325.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1325.jpg?v=20161230" width="110" height="55"  title="Chromebook" alt="Chromebook">
															</div>
															<strong class="title">Chromebook</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/gaming-laptop-d2-1323.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1323.jpg?v=20161230" width="110" height="55"  title="Gaming Laptop" alt="Gaming Laptop">
															</div>
															<strong class="title">Gaming Laptop</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/mainstream-laptop-68-1322.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1322.jpg?v=20161230" width="110" height="55"  title="Mainstream Laptop" alt="Mainstream Laptop">
															</div>
															<strong class="title">Mainstream Laptop</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/mobile-workstation-a9-1479.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1479.jpg?v=20161230" width="110" height="55"  title="Mobile Workstation" alt="Mobile Workstation">
															</div>
															<strong class="title">Mobile Workstation</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/tablets-77-1384.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1384.jpg?v=20161230" width="110" height="55"  title="Tablets" alt="Tablets">
															</div>
															<strong class="title">Tablets</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/ultrabook-laptop-09-1402.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1402.jpg?v=20161230" width="110" height="55"  title="Ultrabook Laptop" alt="Ultrabook Laptop">
															</div>
															<strong class="title">Ultrabooks</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/business-laptop-9e-1324.htm">Business Laptop<span class="qty-count"> (317)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/business-ultrabook-53-1238.htm">Business Ultrabook<span class="qty-count"> (47)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/chromebook-80-1325.htm">Chromebook<span class="qty-count"> (30)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/gaming-laptop-d2-1323.htm">Gaming Laptop<span class="qty-count"> (66)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/laptop-accessories-13-1190.htm">Laptop Accessories<span class="qty-count"> (241)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/laptop-docking-stations-b9-1486.htm">Laptop Docking Stations<span class="qty-count"> (68)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mainstream-laptop-68-1322.htm">Mainstream Laptop<span class="qty-count"> (63)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mobile-workstation-a9-1479.htm">Mobile Workstation<span class="qty-count"> (30)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/tablet-accessories-58-1386.htm">Tablet Accessories<span class="qty-count"> (358)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/tablets-77-1384.htm">Tablets<span class="qty-count"> (113)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ultrabook-laptop-09-1402.htm">Ultrabook Laptop<span class="qty-count"> (10)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Notebook-->
<a href="https://www.ncix.com/article/asus_zenbook_family.htm" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/asus_zenbook_240x425.jpg" alt="Notebook - Asus Zenbook" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
										
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/networking/">Networking</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/network-adapters-f9-1004.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1004.jpg?v=20161230" width="110" height="55"  title="Network Adapters" alt="Network Adapters">
															</div>
															<strong class="title">Network Adapters</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/network-switches-79-1005.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1005.jpg?v=20161230" width="110" height="55"  title="Network Switches" alt="Network Switches">
															</div>
															<strong class="title">Network Switches</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/network-transceivers-61-1394.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1394.jpg?v=20161230" width="110" height="55"  title="Network Transceivers" alt="Network Transceivers">
															</div>
															<strong class="title">Network Transceivers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/powerline-ethernet-29-1211.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1211.jpg?v=20161230" width="110" height="55"  title="Powerline Ethernet" alt="Powerline Ethernet">
															</div>
															<strong class="title">Powerline Ethernet</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/security-firewall-f3-1075.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1075.jpg?v=20161230" width="110" height="55"  title="Security Firewall" alt="Security Firewall">
															</div>
															<strong class="title">Security Firewall</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/wireless-wifi-routers-3d-1046.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1046.jpg?v=20161230" width="110" height="55"  title="Wireless (WiFi) Routers " alt="Wireless (WiFi) Routers ">
															</div>
															<strong class="title">WiFi Routers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/wireless-access-points-80-1277.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1277.jpg?v=20161230" width="110" height="55"  title="Wireless Access Points" alt="Wireless Access Points">
															</div>
															<strong class="title">Wireless Access Points</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/wireless-accessories-c0-1024.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1024.jpg?v=20161230" width="110" height="55"  title="Wireless Accessories" alt="Wireless Accessories">
															</div>
															<strong class="title">Wireless Accessories</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/load-balancer-e6-1444.htm">Load Balancer<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-adapters-f9-1004.htm">Network Adapters<span class="qty-count"> (271)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-cables-63-1508.htm">Network Cables<span class="qty-count"> (15)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-module-1c-1405.htm">Network Module<span class="qty-count"> (32)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-patch-cables-ae-1360.htm">Network Patch Cables<span class="qty-count"> (239)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-switches-79-1005.htm">Network Switches<span class="qty-count"> (469)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-transceivers-61-1394.htm">Network Transceivers<span class="qty-count"> (135)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/poe-injector-a5-1343.htm">POE Injector<span class="qty-count"> (30)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/powerline-ethernet-29-1211.htm">Powerline Ethernet<span class="qty-count"> (35)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/recertified-routers-26-1421.htm">Recertified Routers<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/security-firewall-f3-1075.htm">Security Firewall<span class="qty-count"> (333)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/unified-communication-uc-86-1392.htm">Unified Communication (UC)<span class="qty-count"> (5)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wired-routers-b1-1051.htm">Wired Routers<span class="qty-count"> (96)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wireless-wifi-routers-3d-1046.htm">Wireless (WiFi) Routers <span class="qty-count"> (133)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wireless-access-points-80-1277.htm">Wireless Access Points<span class="qty-count"> (314)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wireless-accessories-c0-1024.htm">Wireless Accessories<span class="qty-count"> (91)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wireless-bridge-55-1204.htm">Wireless Bridge<span class="qty-count"> (69)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!-- Networking -->
<a href="https://www.ncix.com/article/asus_ACextenders.htm" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/asus_routerRT/asus_routerRT_240x425.jpg" alt="Networking - Asus FAST" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/television/">TV & Home Theatre</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/30-39-tvs-70-1235.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1235.jpg?v=20161230" width="110" height="55"  title="30&quot; - 39&quot; TVs" alt="30&quot; - 39&quot; TVs">
															</div>
															<strong class="title">30" - 39" TVs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/40-45-tvs-a7-1236.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1236.jpg?v=20161230" width="110" height="55"  title="40&quot; - 45&quot; TVs" alt="40&quot; - 45&quot; TVs">
															</div>
															<strong class="title">40" - 45" TVs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/46-49-tvs-4e-1525.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1525.jpg?v=20161230" width="110" height="55"  title="46&quot; - 49&quot; TVs" alt="46&quot; - 49&quot; TVs">
															</div>
															<strong class="title">46" - 49" TVs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/50-59-tvs-39-1436.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1436.jpg?v=20161230" width="110" height="55"  title="50&quot; - 59&quot; TVs" alt="50&quot; - 59&quot; TVs">
															</div>
															<strong class="title">50" - 59" TVs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/60-up-tvs-af-1437.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1437.jpg?v=20161230" width="110" height="55"  title="60&quot; &amp; Up TVs" alt="60&quot; &amp; Up TVs">
															</div>
															<strong class="title">60" & Up TVs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/digital-picture-frames-0d-1383.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1383.jpg?v=20161230" width="110" height="55"  title="Digital Picture Frames" alt="Digital Picture Frames">
															</div>
															<strong class="title">Digital Picture Frames</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/home-theater-projectors-da-1227.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1227.jpg?v=20161230" width="110" height="55"  title="Home Theater Projectors" alt="Home Theater Projectors">
															</div>
															<strong class="title">Home Theater Projectors</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/tv-accessories-bd-1270.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1270.jpg?v=20161230" width="110" height="55"  title="TV Accessories" alt="TV Accessories">
															</div>
															<strong class="title">TV Accessories</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/19-29-tvs-d3-1234.htm">19" - 29" TVs<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/30-39-tvs-70-1235.htm">30" - 39" TVs<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/40-45-tvs-a7-1236.htm">40" - 45" TVs<span class="qty-count"> (13)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/46-49-tvs-4e-1525.htm">46" - 49" TVs<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/50-59-tvs-39-1436.htm">50" - 59" TVs<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/60-up-tvs-af-1437.htm">60" & Up TVs<span class="qty-count"> (13)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/digital-picture-frames-0d-1383.htm">Digital Picture Frames<span class="qty-count"> (6)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/home-theater-projectors-da-1227.htm">Home Theater Projectors<span class="qty-count"> (14)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/tv-accessories-bd-1270.htm">TV Accessories<span class="qty-count"> (1)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--TV & Home Theatres-->
<a href="https://www.ncix.com/clearance/" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/clearanceCA_240x425-new.jpg" border="0" display="block" alt="Online only warehouse clearance event" /></a>
<!--
<a href="https://www.ncix.com/subpromo/1667.htm" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/dropdown_bnr/HDTV-Promo_240x425.jpg" border="0" display="block" /></a>
-->
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/Mobile-accessories/">Mobile Accessories</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/accessories-3b-1189.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1189.jpg?v=20161230" width="110" height="55"  title="Accessories" alt="Accessories">
															</div>
															<strong class="title">Accessories</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/bluetooth-headsets-c3-3053.htm">
															<div class="image-holder">
																<img src="/_img/space.gif" width="110" height="55"  title="Bluetooth Headsets" alt="Bluetooth Headsets">
															</div>
															<strong class="title">Bluetooth Headsets</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/cables-adapters-2a-1365.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1365.jpg?v=20161230" width="110" height="55"  title="Cables &amp; Adapters" alt="Cables &amp; Adapters">
															</div>
															<strong class="title">Cables & Adapters</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/car-accessories-cf-1509.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1509.jpg?v=20161230" width="110" height="55"  title="Car Accessories" alt="Car Accessories">
															</div>
															<strong class="title">Car Accessories</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/docks-stands-e3-1439.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1439.jpg?v=20161230" width="110" height="55"  title="Docks &amp; Stands" alt="Docks &amp; Stands">
															</div>
															<strong class="title">Docks & Stands</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/mobile-phone-headsets-c0-1400.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1400.jpg?v=20161230" width="110" height="55"  title="Mobile Phone Headsets" alt="Mobile Phone Headsets">
															</div>
															<strong class="title">Mobile Phone Headsets</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/phone-cases-27-1233.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1233.jpg?v=20161230" width="110" height="55"  title="Phone Cases" alt="Phone Cases">
															</div>
															<strong class="title">Phone Cases</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/portable-chargers-61-1095.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1095.jpg?v=20161230" width="110" height="55"  title="Portable Chargers" alt="Portable Chargers">
															</div>
															<strong class="title">Portable Chargers</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/accessories-3b-1189.htm">Accessories<span class="qty-count"> (234)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/bluetooth-headsets-c3-3053.htm">Bluetooth Headsets<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cables-adapters-2a-1365.htm">Cables & Adapters<span class="qty-count"> (1501)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/car-accessories-cf-1509.htm">Car Accessories<span class="qty-count"> (29)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/docks-stands-e3-1439.htm">Docks & Stands<span class="qty-count"> (18)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mobile-phone-headsets-c0-1400.htm">Mobile Phone Headsets<span class="qty-count"> (45)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/phone-cases-27-1233.htm">Phone Cases<span class="qty-count"> (207)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/portable-chargers-61-1095.htm">Portable Chargers<span class="qty-count"> (66)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/power-chargers-6c-1182.htm">Power & Chargers<span class="qty-count"> (176)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/screen-care-styluses-1c-1443.htm">Screen Care & Styluses<span class="qty-count"> (63)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/selfie-sticks-tripods-0f-3044.htm">Selfie Sticks & Tripods<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/smart-accessories-87-3054.htm">Smart Accessories<span class="qty-count"> (12)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/category/mobile-phones-90-1216.htm">Mobile Phones</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/mobile-phone-accessories-7f-1335.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1335.jpg?v=20161230" width="110" height="55"  title="Mobile Phone Accessories" alt="Mobile Phone Accessories">
															</div>
															<strong class="title">Mobile Phone Accessories</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/unlocked-smartphones-28-1216.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1216.jpg?v=20161230" width="110" height="55"  title="Unlocked Smartphones" alt="Unlocked Smartphones">
															</div>
															<strong class="title">Unlocked Smartphones</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mobile-phone-accessories-7f-1335.htm">Mobile Phone Accessories<span class="qty-count"> (340)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/unlocked-smartphones-28-1216.htm">Unlocked Smartphones<span class="qty-count"> (109)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Mobile Phones-->
<a href="https://www.ncix.com/category/mobile-phones-90-1216.htm" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/promotions/UnlockedMobile-Promo_240x425.jpg" alt="Mobile Phones - Unlocked Phones" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/majorcategory/monitors-23-102.htm">Monitors</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/4k-monitors-06-1494.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1494.jpg?v=20161230" width="110" height="55"  title="4K Monitors" alt="4K Monitors">
															</div>
															<strong class="title">4K Monitors</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/curved-monitors-30-3e-1352.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1352.jpg?v=20161230" width="110" height="55"  title="Curved Monitors 30&quot; +" alt="Curved Monitors 30&quot; +">
															</div>
															<strong class="title">Curved Monitors </strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
														
													
													<li>
														<a href="https://www.ncix.com/category/digital-signage-monitor-45-76-1527.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1527.jpg?v=20161230" width="110" height="55"  title="Digital Signage Monitor 45&quot; +" alt="Digital Signage Monitor 45&quot; +">
															</div>
															<strong class="title">Digital Signage</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/gaming-monitors-68-1186.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1186.jpg?v=20161230" width="110" height="55"  title="Gaming Monitors" alt="Gaming Monitors">
															</div>
															<strong class="title">Gaming Monitors</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/lcd-monitors-69-1003.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1003.jpg?v=20161230" width="110" height="55"  title="LCD Monitors" alt="LCD Monitors">
															</div>
															<strong class="title">LCD Monitors</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/lcd-monitors-30-32-1348.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1348.jpg?v=20161230" width="110" height="55"  title="LCD Monitors 30&quot;+" alt="LCD Monitors 30&quot;+">
															</div>
															<strong class="title">LCD Monitors 30"+</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/stands-mounts-18-1054.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1054.jpg?v=20161230" width="110" height="55"  title="Stands &amp; Mounts" alt="Stands &amp; Mounts">
															</div>
															<strong class="title">Stands & Mounts</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/ultrawide-monitors-04-1185.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1185.jpg?v=20161230" width="110" height="55"  title="Ultrawide Monitors" alt="Ultrawide Monitors">
															</div>
															<strong class="title">Ultrawide Monitors</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/4k-monitors-06-1494.htm">4K Monitors<span class="qty-count"> (18)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/4k-monitors-30-ba-1002.htm">4K Monitors 30"+<span class="qty-count"> (9)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/curved-monitors-44-1526.htm">Curved Monitors<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/curved-monitors-30-3e-1352.htm">Curved Monitors 30" +<span class="qty-count"> (20)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/digital-signage-monitor-4b-1496.htm">Digital Signage Monitor<span class="qty-count"> (37)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/digital-signage-monitor-30-to-45-07-1497.htm">Digital Signage Monitor 30" to 45"<span class="qty-count"> (27)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/digital-signage-monitor-45-76-1527.htm">Digital Signage Monitor 45" +<span class="qty-count"> (50)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/gaming-monitors-68-1186.htm">Gaming Monitors<span class="qty-count"> (76)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/graphics-cad-cam-monitors-a0-1001.htm">Graphics CAD/CAM Monitors<span class="qty-count"> (9)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/lcd-monitors-69-1003.htm">LCD Monitors<span class="qty-count"> (364)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/lcd-monitors-30-32-1348.htm">LCD Monitors 30"+<span class="qty-count"> (37)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/monitor-accessories-e0-1327.htm">Monitor Accessories<span class="qty-count"> (94)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/stands-mounts-18-1054.htm">Stands & Mounts<span class="qty-count"> (246)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/touchscreen-monitors-e0-1042.htm">Touchscreen Monitors<span class="qty-count"> (194)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ultrawide-monitors-04-1185.htm">Ultrawide Monitors<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ultrawide-monitors-30-43-1495.htm">Ultrawide Monitors 30"+<span class="qty-count"> (3)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Monitors-->
<a href="https://www.ncix.com/article/asus_PGfamily.htm" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/asus_PGfamily/asus_PGfamily_240x425.jpg" alt="Monitors - Asus ROG Swift Gaming" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/computers/">Desktop</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/all-in-one-pcs-46-1336.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1336.jpg?v=20161230" width="110" height="55"  title="All-in-One PCs" alt="All-in-One PCs">
															</div>
															<strong class="title">All-in-One PCs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/barebone-computer-3a-1446.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1446.jpg?v=20161230" width="110" height="55"  title="Barebone Computer" alt="Barebone Computer">
															</div>
															<strong class="title">Barebone Computer</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/business-desktops-4f-1357.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1357.jpg?v=20161230" width="110" height="55"  title="Business Desktops" alt="Business Desktops">
															</div>
															<strong class="title">Business Desktops</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/business-mini-pcs-02-1363.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1363.jpg?v=20161230" width="110" height="55"  title="Business Mini PCs" alt="Business Mini PCs">
															</div>
															<strong class="title">Business Mini PCs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/desktop-computers-f0-1356.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1356.jpg?v=20161230" width="110" height="55"  title="Desktop Computers" alt="Desktop Computers">
															</div>
															<strong class="title">Desktop Computers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/gaming-desktop-20-1413.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1413.jpg?v=20161230" width="110" height="55"  title="Gaming Desktop" alt="Gaming Desktop">
															</div>
															<strong class="title">Gaming Desktop</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/ncix-desktops-ae-1491.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1491.jpg?v=20161230" width="110" height="55"  title="NCIX Desktops" alt="NCIX Desktops">
															</div>
															<strong class="title">NCIX Desktops</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/servers-31-1072.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1072.jpg?v=20161230" width="110" height="55"  title="Servers" alt="Servers">
															</div>
															<strong class="title">Servers</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/all-in-one-pcs-46-1336.htm">All-in-One PCs<span class="qty-count"> (25)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/barebone-computer-3a-1446.htm">Barebone Computer<span class="qty-count"> (43)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/barebones-server-8c-1076.htm">Barebones Server<span class="qty-count"> (129)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/barebones-workstation-d1-1213.htm">Barebones Workstation<span class="qty-count"> (11)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/business-desktops-4f-1357.htm">Business Desktops<span class="qty-count"> (215)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/business-mini-pcs-02-1363.htm">Business Mini PCs<span class="qty-count"> (59)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/computer-accessories-85-1041.htm">Computer Accessories<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/consumer-mini-pcs-62-1113.htm">Consumer Mini PCs<span class="qty-count"> (29)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/desktop-computers-f0-1356.htm">Desktop Computers<span class="qty-count"> (28)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/gaming-desktop-20-1413.htm">Gaming Desktop<span class="qty-count"> (23)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ncix-desktops-ae-1491.htm">NCIX Desktops<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/nx-fusion-assembly-options-1c-1217.htm">NX Fusion Assembly Options<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/server-accessories-f4-1276.htm">Server Accessories<span class="qty-count"> (347)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/servers-31-1072.htm">Servers<span class="qty-count"> (187)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/warranty-options-7f-1334.htm">Warranty Options<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/workstations-9b-1395.htm">Workstations<span class="qty-count"> (11)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--DesktopPC-->
<a href="https://www.ncix.com/article/Entra-Home-Series-4.htm" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/NCIX-PC/Entra-Home-2016-240w.jpg" border="0" display="block" alt="Entra Home Series Business PCs"/></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/electronics/">Electronics</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/dvd-blu-ray-players-b6-1083.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1083.jpg?v=20161230" width="110" height="55"  title="DVD &amp; Blu-Ray Players" alt="DVD &amp; Blu-Ray Players">
															</div>
															<strong class="title">DVD & Blu-Ray Players</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/headphones-8d-1318.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1318.jpg?v=20161230" width="110" height="55"  title="Headphones" alt="Headphones">
															</div>
															<strong class="title">Headphones</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/home-automation-99-1337.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1337.jpg?v=20161230" width="110" height="55"  title="Home Automation" alt="Home Automation">
															</div>
															<strong class="title">Home Automation</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/home-theater-in-a-box-a5-1244.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1244.jpg?v=20161230" width="110" height="55"  title="Home Theater in a Box" alt="Home Theater in a Box">
															</div>
															<strong class="title">Home Theater in a Box</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/media-players-71-1331.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1331.jpg?v=20161230" width="110" height="55"  title="Media Players" alt="Media Players">
															</div>
															<strong class="title">Media Players</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/microphones-voice-recorders-c7-1268.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1268.jpg?v=20161230" width="110" height="55"  title="Microphones &amp; Voice Recorders" alt="Microphones &amp; Voice Recorders">
															</div>
															<strong class="title">Microphones & Voice Recorders</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/portable-speakers-and-docks-71-1482.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1482.jpg?v=20161230" width="110" height="55"  title="Portable Speakers and Docks" alt="Portable Speakers and Docks">
															</div>
															<strong class="title">Portable Speakers and Docks</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/soundbars-and-soundbases-5c-1481.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1481.jpg?v=20161230" width="110" height="55"  title="Soundbars and Soundbases" alt="Soundbars and Soundbases">
															</div>
															<strong class="title">Soundbars and Soundbases</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/av-furniture-6e-1259.htm">AV Furniture<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/accessories-3b-1274.htm">Accessories<span class="qty-count"> (73)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/audio-cables-a2-1008.htm">Audio Cables<span class="qty-count"> (13)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cd-players-18-1262.htm">CD Players<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/camcorders-7b-1084.htm">Camcorders<span class="qty-count"> (11)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/camera-accessories-c9-1176.htm">Camera Accessories<span class="qty-count"> (160)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/car-audio-0a-1269.htm">Car Audio<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/clock-radios-b5-1480.htm">Clock Radios<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/corded-phones-answering-machines-16-1250.htm">Corded Phones & Answering Machines<span class="qty-count"> (20)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cordless-phones-e9-1223.htm">Cordless Phones<span class="qty-count"> (13)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/dacs-and-amplifiers-c4-1515.htm">DACs and Amplifiers<span class="qty-count"> (11)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/dvd-blu-ray-players-b6-1083.htm">DVD & Blu-Ray Players<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/dashcams-c1-1493.htm">Dashcams<span class="qty-count"> (23)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/digital-cameras-6c-1020.htm">Digital Cameras<span class="qty-count"> (42)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/frs-walkietalkies-15-1267.htm">FRS / WalkieTalkies<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/hdmi-switches-8a-1418.htm">HDMI Switches<span class="qty-count"> (15)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/headphone-accessories-5b-1330.htm">Headphone Accessories<span class="qty-count"> (39)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/headphones-8d-1318.htm">Headphones<span class="qty-count"> (269)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/headphones-headsets-1c-1536.htm">Headphones / Headsets<span class="qty-count"> (84)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/home-automation-99-1337.htm">Home Automation<span class="qty-count"> (22)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/home-theater-in-a-box-a5-1244.htm">Home Theater in a Box<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mp3-players-94-1086.htm">MP3 Players<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/media-players-71-1331.htm">Media Players<span class="qty-count"> (40)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/microphones-voice-recorders-c7-1268.htm">Microphones & Voice Recorders<span class="qty-count"> (84)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/portable-media-players-19-1351.htm">Portable Media Players<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/portable-speakers-and-docks-71-1482.htm">Portable Speakers and Docks<span class="qty-count"> (82)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/powered-speakers-58-1510.htm">Powered Speakers<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/receivers-amplifiers-97-1243.htm">Receivers & Amplifiers<span class="qty-count"> (5)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/remote-controls-accessories-7f-1419.htm">Remote Controls & Accessories<span class="qty-count"> (17)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/soundbars-and-soundbases-5c-1481.htm">Soundbars and Soundbases<span class="qty-count"> (5)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/speaker-stands-accessories-3e-1109.htm">Speaker Stands & Accessories<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/speakers-e7-1242.htm">Speakers<span class="qty-count"> (113)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/sports-helmet-cameras-f3-1434.htm">Sports & Helmet Cameras<span class="qty-count"> (27)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/stereo-systems-e8-1245.htm">Stereo Systems<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/turntables-0c-1502.htm">Turntables<span class="qty-count"> (25)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/voip-internet-phone-0f-1253.htm">VOIP / Internet Phone<span class="qty-count"> (152)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/video-conference-71-1200.htm">Video Conference<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/video-extender-75-1237.htm">Video Extender<span class="qty-count"> (46)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/voip-adapters-26-1203.htm">VoIP Adapters<span class="qty-count"> (21)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/voice-conference-59-1490.htm">Voice Conference<span class="qty-count"> (26)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wall-mounts-1b-1232.htm">Wall Mounts<span class="qty-count"> (144)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wearables-watches-d4-1411.htm">Wearables & Watches<span class="qty-count"> (76)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wireless-audio-97-1520.htm">Wireless Audio<span class="qty-count"> (16)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/wireless-hdmi-a8-1368.htm">Wireless HDMI<span class="qty-count"> (9)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!-- Electronics -->
<a href="https://search.ncix.com/search/?qcatid=0&q=kingston+cloud" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/hyperX_cloud2_240x425.jpg" alt="Electronics - HyperX Cloud II Headsets" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
										
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/accessories/">Accessories</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/batteries-power-2c-100.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/100.jpg?v=20161230" width="110" height="55"  title="Batteries &amp; Power" alt="Batteries &amp; Power">
															</div>
															<strong class="title">Batteries & Power</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/cables-f7-1168.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1168.jpg?v=20161230" width="110" height="55"  title="Cables " alt="Cables ">
															</div>
															<strong class="title">Cables </strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/carrying-cases-33-1022.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1022.jpg?v=20161230" width="110" height="55"  title="Carrying Cases" alt="Carrying Cases">
															</div>
															<strong class="title">Carrying Cases</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/computer-speakers-57-103.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/103.jpg?v=20161230" width="110" height="55"  title="Computer Speakers" alt="Computer Speakers">
															</div>
															<strong class="title">Computer Speakers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/gaming-chairs-5e-1366.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1366.jpg?v=20161230" width="110" height="55"  title="Gaming Chairs" alt="Gaming Chairs">
															</div>
															<strong class="title">Gaming Chairs</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/gaming-headsets-e9-1231.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1231.jpg?v=20161230" width="110" height="55"  title="Gaming Headsets" alt="Gaming Headsets">
															</div>
															<strong class="title">Gaming Headsets</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/mouse-pads-86-1193.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1193.jpg?v=20161230" width="110" height="55"  title="Mouse Pads" alt="Mouse Pads">
															</div>
															<strong class="title">Mouse Pads</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/power-management-bd-1036.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1036.jpg?v=20161230" width="110" height="55"  title="Power Management" alt="Power Management">
															</div>
															<strong class="title">Power Management</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/adapters-b0-1256.htm">Adapters <span class="qty-count"> (176)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/batteries-power-2c-100.htm">Batteries & Power<span class="qty-count"> (410)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/blank-media-2d-1010.htm">Blank Media<span class="qty-count"> (42)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/cables-f7-1168.htm">Cables <span class="qty-count"> (1805)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/calculators-27-1114.htm">Calculators<span class="qty-count"> (22)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/carrying-cases-33-1022.htm">Carrying Cases<span class="qty-count"> (77)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/clocks-ac-1115.htm">Clocks<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/computer-speakers-57-103.htm">Computer Speakers<span class="qty-count"> (24)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/document-holders-bd-1457.htm">Document Holders<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/extended-warranties-ca-1466.htm">Extended Warranties<span class="qty-count"> (546)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/gaming-chairs-5e-1366.htm">Gaming Chairs<span class="qty-count"> (117)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/gaming-headsets-e9-1231.htm">Gaming Headsets<span class="qty-count"> (150)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/htpc-accessories-c0-1174.htm">HTPC Accessories<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/kvm-cables-97-1514.htm">KVM Cables<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/kvms-66-1009.htm">KVMs<span class="qty-count"> (194)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/keyboard-trays-c5-1456.htm">Keyboard Trays<span class="qty-count"> (27)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mac-accessories-53-1404.htm">Mac Accessories<span class="qty-count"> (18)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mac-memory-c8-1266.htm">Mac Memory<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/misc-office-f5-1163.htm">Misc Office<span class="qty-count"> (12)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mobile-racks-f9-1273.htm">Mobile Racks<span class="qty-count"> (26)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/modding-dc-1112.htm">Modding<span class="qty-count"> (272)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/mouse-pads-86-1193.htm">Mouse Pads<span class="qty-count"> (77)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ncix-express-exchange-care-coverage-plan-d8-1349.htm">NCIX Express Exchange & Care Coverage Plan<span class="qty-count"> (32)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ncix-pc-promotional-39-1483.htm">NCIX PC Promotional<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ncix-promotional-5c-1179.htm">NCIX Promotional<span class="qty-count"> (113)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ncix-service-replacement-parts-53-1459.htm">NCIX Service Replacement Parts<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/office-ergonomics-51-1433.htm">Office Ergonomics<span class="qty-count"> (24)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/others-8e-1065.htm">Others<span class="qty-count"> (793)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/pens-73-1116.htm">Pens<span class="qty-count"> (26)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/power-cables-0a-1511.htm">Power Cables<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/power-management-bd-1036.htm">Power Management<span class="qty-count"> (613)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/powered-2-0-speakers-2e-1469.htm">Powered 2.0 Speakers<span class="qty-count"> (5)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/raid-card-accessories-ea-1397.htm">RAID Card Accessories<span class="qty-count"> (24)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/rackmount-display-kvm-55-1222.htm">Rackmount Display KVM<span class="qty-count"> (12)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/shipping-materials-f4-1470.htm">Shipping Materials<span class="qty-count"> (10)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/shredders-64-1420.htm">Shredders<span class="qty-count"> (30)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/special-promotions-9e-1350.htm">Special Promotions<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/stands-4b-1489.htm">Stands<span class="qty-count"> (22)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/surge-protection-ee-1529.htm">Surge Protection<span class="qty-count"> (177)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/thermal-compound-16-1220.htm">Thermal Compound<span class="qty-count"> (13)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/usb-add-ons-61-1025.htm">USB Add-Ons<span class="qty-count"> (97)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/usb-speakers-a5-1412.htm">USB Speakers<span class="qty-count"> (10)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!-- Accessories -->
<a href="https://search.ncix.com/search/?qcatid=0&q=ekwb+predator" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/ekwb-promo/EKWB_Predator_240x425.jpg" border="0" display="block" alt="4K Streaming Advanced Gaming Android TV NVIDIA SHIELD" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/gadget/">Gadget & Toys</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/drones-1b-1183.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1183.jpg?v=20161230" width="110" height="55"  title="Drones" alt="Drones">
															</div>
															<strong class="title">Drones</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/gadget-toys-08-1166.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1166.jpg?v=20161230" width="110" height="55"  title="Gadget &amp; Toys" alt="Gadget &amp; Toys">
															</div>
															<strong class="title">Gadget & Toys</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/handheld-3d-printing-3b-1364.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1364.jpg?v=20161230" width="110" height="55"  title="Handheld 3D Printing" alt="Handheld 3D Printing">
															</div>
															<strong class="title">Handheld 3D Printing</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/remote-control-toys-7b-1258.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1258.jpg?v=20161230" width="110" height="55"  title="Remote Control Toys" alt="Remote Control Toys">
															</div>
															<strong class="title">Remote Control Toys</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/drones-1b-1183.htm">Drones<span class="qty-count"> (79)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/electric-transport-37-1151.htm">Electric Transport<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/flashlights-33-1416.htm">Flashlights<span class="qty-count"> (2)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/gadget-toys-08-1166.htm">Gadget & Toys<span class="qty-count"> (33)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/handheld-3d-printing-3b-1364.htm">Handheld 3D Printing<span class="qty-count"> (5)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/remote-control-toys-7b-1258.htm">Remote Control Toys<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/sewing-machine-58-1088.htm">Sewing Machine<span class="qty-count"> (2)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Gadget & Toys-->
<a href="https://search.ncix.com/search/?qcatid=0&q=drone" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/dji_camera_240x425.jpg" alt="Gadget &amp; Toys - DJI Drones" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/game-consoles/">Game Consoles</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/android-gaming-1d-1107.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1107.jpg?v=20161230" width="110" height="55"  title="Android Gaming" alt="Android Gaming">
															</div>
															<strong class="title">Android Gaming</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/console-accessories-85-1332.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1332.jpg?v=20161230" width="110" height="55"  title="Console Accessories" alt="Console Accessories">
															</div>
															<strong class="title">Console Accessories</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/controllers-45-1214.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1214.jpg?v=20161230" width="110" height="55"  title="Controllers" alt="Controllers">
															</div>
															<strong class="title">Controllers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/playstation-4-a8-1445.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1445.jpg?v=20161230" width="110" height="55"  title="PlayStation 4" alt="PlayStation 4">
															</div>
															<strong class="title">PlayStation 4</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/video-game-capture-cards-88-1175.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1175.jpg?v=20161230" width="110" height="55"  title="Video Game Capture Cards" alt="Video Game Capture Cards">
															</div>
															<strong class="title">Video Game Capture Cards</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/xbox-one-a0-1449.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1449.jpg?v=20161230" width="110" height="55"  title="Xbox One" alt="Xbox One">
															</div>
															<strong class="title">Xbox One</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/android-gaming-1d-1107.htm">Android Gaming<span class="qty-count"> (6)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/console-accessories-85-1332.htm">Console Accessories<span class="qty-count"> (21)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/controllers-45-1214.htm">Controllers<span class="qty-count"> (11)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/playstation-4-a8-1445.htm">PlayStation 4<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/video-game-capture-cards-88-1175.htm">Video Game Capture Cards<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/xbox-one-a0-1449.htm">Xbox One<span class="qty-count"> (12)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Consoles-->
<a href="https://search.ncix.com/search/?qcatid=0&q=shield+android" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/nvidia-shield-androidtv/nvidia-shieldtv_240x425.jpg" alt="Consoles - Nvidia Shield" border="0" display="block" /></a>
<!--
<a href="https://www.ncix.com/game-consoles/" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/department_bnr/Department-Consoles-01.jpg" border="0" display="block" /></a>
-->
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/printers/">Printers</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/3d-printers-55-1472.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1472.jpg?v=20161230" width="110" height="55"  title="3D Printers" alt="3D Printers">
															</div>
															<strong class="title">3D Printers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/ink-cartridges-55-1196.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1196.jpg?v=20161230" width="110" height="55"  title="Ink Cartridges" alt="Ink Cartridges">
															</div>
															<strong class="title">Ink Cartridges</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/inkjet-printers-7f-1031.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1031.jpg?v=20161230" width="110" height="55"  title="Inkjet Printers" alt="Inkjet Printers">
															</div>
															<strong class="title">Inkjet Printers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/label-makers-d0-1424.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1424.jpg?v=20161230" width="110" height="55"  title="Label Makers" alt="Label Makers">
															</div>
															<strong class="title">Label Makers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/large-format-printers-b3-1060.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1060.jpg?v=20161230" width="110" height="55"  title="Large Format Printers" alt="Large Format Printers">
															</div>
															<strong class="title">Large Format Printers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/laser-printers-8a-1032.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1032.jpg?v=20161230" width="110" height="55"  title="Laser Printers" alt="Laser Printers">
															</div>
															<strong class="title">Laser Printers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/multifunction-printers-06-1045.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1045.jpg?v=20161230" width="110" height="55"  title="Multifunction Printers" alt="Multifunction Printers">
															</div>
															<strong class="title">Multifunction Printers</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/toner-drum-49-1197.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1197.jpg?v=20161230" width="110" height="55"  title="Toner &amp; Drum" alt="Toner &amp; Drum">
															</div>
															<strong class="title">Toner & Drum</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/3d-printers-55-1472.htm">3D Printers<span class="qty-count"> (8)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/3d-printing-filament-2b-1473.htm">3D Printing Filament<span class="qty-count"> (44)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/dot-matrix-printers-54-1030.htm">Dot Matrix Printers<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/floor-standing-printers-74-1422.htm">Floor Standing Printers<span class="qty-count"> (23)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ink-cartridges-55-1196.htm">Ink Cartridges<span class="qty-count"> (587)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/inkjet-printers-7f-1031.htm">Inkjet Printers<span class="qty-count"> (13)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/label-makers-d0-1424.htm">Label Makers<span class="qty-count"> (22)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/labels-13-1198.htm">Labels<span class="qty-count"> (121)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/large-format-printers-b3-1060.htm">Large Format Printers<span class="qty-count"> (7)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/laser-printers-8a-1032.htm">Laser Printers<span class="qty-count"> (98)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/multifunction-printers-06-1045.htm">Multifunction Printers<span class="qty-count"> (102)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/photo-paper-db-1199.htm">Photo Paper<span class="qty-count"> (31)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/photo-printers-3a-1353.htm">Photo Printers<span class="qty-count"> (9)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/print-servers-eb-1033.htm">Print Servers<span class="qty-count"> (6)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/printer-accessories-a3-1321.htm">Printer Accessories<span class="qty-count"> (443)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/specialty-printers-a6-1226.htm">Specialty Printers<span class="qty-count"> (28)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/toner-drum-49-1197.htm">Toner & Drum<span class="qty-count"> (917)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Printers-->
<a href="https://www.ncix.com/tonerfinder/" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/HP-Toner/HP-Toner-Finder-240w.jpg" alt="Printers - Ink and Toner Finder" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/apparel/">Apparel</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/ncix-tech-tips-12-3060.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/3060.jpg?v=20161230" width="110" height="55"  title="NCIX Tech Tips" alt="NCIX Tech Tips">
															</div>
															<strong class="title">NCIX Tech Tips</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/nx-fusion-7b-3041.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/3041.jpg?v=20161230" width="110" height="55"  title="NX Fusion" alt="NX Fusion">
															</div>
															<strong class="title">NX Fusion</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/sunny-clouds-bd-3042.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/3042.jpg?v=20161230" width="110" height="55"  title="Sunny Clouds" alt="Sunny Clouds">
															</div>
															<strong class="title">Sunny Clouds</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/ncix-tech-tips-12-3060.htm">NCIX Tech Tips<span class="qty-count"> (14)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/nx-fusion-7b-3041.htm">NX Fusion<span class="qty-count"> (35)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/sunny-clouds-bd-3042.htm">Sunny Clouds<span class="qty-count"> (183)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
											</div>
										</div>	
									</li>
								
									
									
									
										
									
									<li >
										
										
										<a href="https://www.ncix.com/software/">Software</a>
										
									
										
										<div class="category-drop">
											<ul class="products-list">
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/accounting-and-finance-4f-1454.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1454.jpg?v=20161230" width="110" height="55"  title="Accounting and Finance" alt="Accounting and Finance">
															</div>
															<strong class="title">Accounting and Finance</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/business-6a-1034.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1034.jpg?v=20161230" width="110" height="55"  title="Business" alt="Business">
															</div>
															<strong class="title">Business</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/graphic-apps-6c-1110.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1110.jpg?v=20161230" width="110" height="55"  title="Graphic Apps" alt="Graphic Apps">
															</div>
															<strong class="title">Graphic Apps</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/operating-systems-22-1055.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1055.jpg?v=20161230" width="110" height="55"  title="Operating Systems" alt="Operating Systems">
															</div>
															<strong class="title">Operating Systems</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/security-privacy-a5-1049.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1049.jpg?v=20161230" width="110" height="55"  title="Security &amp; Privacy" alt="Security &amp; Privacy">
															</div>
															<strong class="title">Security & Privacy</strong>
														</a>
													</li>
												
													 	
													
														
													
													
													
													<li>
														<a href="https://www.ncix.com/category/system-utilities-fe-1050.htm">
															<div class="image-holder">
																<img src="https://d1sfu4378rr01a.cloudfront.net/categoryimages/1050.jpg?v=20161230" width="110" height="55"  title="System Utilities" alt="System Utilities">
															</div>
															<strong class="title">System Utilities</strong>
														</a>
													</li>
												
												
											</ul>
											<div class="sub-category-holder">
												<strong class="title">more categories</strong>
												<div class="jcf-scrollable">
													<ul class="sub-category-list">
													
														 	
														<li>
															<a href="https://www.ncix.com/category/accounting-and-finance-4f-1454.htm">Accounting and Finance<span class="qty-count"> (15)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/audio-multimedia-30-1369.htm">Audio & Multimedia<span class="qty-count"> (3)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/backup-and-restore-1b-1035.htm">Backup and Restore<span class="qty-count"> (168)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/business-6a-1034.htm">Business<span class="qty-count"> (40)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/communications-f9-1154.htm">Communications<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/education-bf-1170.htm">Education<span class="qty-count"> (4)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/graphic-apps-6c-1110.htm">Graphic Apps<span class="qty-count"> (20)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/licensing-for-networking-hardware-83-3056.htm">Licensing for Networking Hardware<span class="qty-count"> (9)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/network-internet-15-1370.htm">Network & Internet<span class="qty-count"> (101)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/oem-79-1064.htm">OEM <span class="qty-count"> (20)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/operating-systems-22-1055.htm">Operating Systems<span class="qty-count"> (46)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/screen-savers-7b-1380.htm">Screen Savers<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/security-privacy-a5-1049.htm">Security & Privacy<span class="qty-count"> (67)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/server-and-network-management-software-84-3057.htm">Server and Network Management Software<span class="qty-count"> (1)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/server-and-virtualization-92-1455.htm">Server and Virtualization<span class="qty-count"> (29)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/system-utilities-fe-1050.htm">System Utilities<span class="qty-count"> (26)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/volume-licensing-b6-1218.htm">Volume Licensing<span class="qty-count"> (480)</span></a>
														</li>
													
														 	
														<li>
															<a href="https://www.ncix.com/category/web-development-32-1371.htm">Web Development<span class="qty-count"> (3)</span></a>
														</li>
														
													</ul>
												</div>
											</div>
											<div class="banner-holder">
												
												
												
													<!--Software-->
<a href="https://search.ncix.com/search/?qcatid=0&q=microsoft+windows+10" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/ms_win10_240x425.jpg" alt="Software - Microsoft Windows 10" border="0" display="block" /></a>
												
												
												
											</div>
										</div>	
									</li>
								
									
									
												
						</ul>
					</div>
				</li>
					
				
				<li>
				
					<a href="#" alt="Brands" title="Brands">Brands</a>
					<div class="drop">
						<div class="drop-holder" style="height:400px;">
							<ul class="logo-list" style="padding-top:15px;padding-left:10px;">
								
									
									<li><a href="https://www.ncix.com/vendor/amd-06-36.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/36-s.gif" width="80" height="40" alt="AMD" title="AMD"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/asus-89-25.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/25-s.gif" width="80" height="40" alt="ASUS" title="ASUS"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/be-quiet-dc-4703.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4703-s.gif" width="80" height="40" alt="be quiet!" title="be quiet!"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/bitfenix-c8-4371.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4371-s.gif" width="80" height="40" alt="BitFenix" title="BitFenix"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/brother-d7-29.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/29-s.gif" width="80" height="40" alt="Brother" title="Brother"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/dji-9e-5093.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/5093-s.gif" width="80" height="40" alt="DJI" title="DJI"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/ducky-8a-4689.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4689-s.gif" width="80" height="40" alt="Ducky" title="Ducky"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/evga-eb-3465.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/3465-s.gif" width="80" height="40" alt="eVGA" title="eVGA"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/fractal-design-4f-4259.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4259-s.gif" width="80" height="40" alt="Fractal Design" title="Fractal Design"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/gigabyte-fb-3.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/3-s.gif" width="80" height="40" alt="Gigabyte" title="Gigabyte"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/intel-55-28.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/28-s.gif" width="80" height="40" alt="Intel" title="Intel"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/kanto-b4-4884.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4884-s.gif" width="80" height="40" alt="Kanto" title="Kanto"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/linke-0d-4820.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4820-s.gif" width="80" height="40" alt="Linke" title="Linke"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/logitech-75-69.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/69-s.gif" width="80" height="40" alt="Logitech" title="Logitech"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/microsoft-a7-4.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4-s.gif" width="80" height="40" alt="Microsoft" title="Microsoft"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/msi-e2-74.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/74-s.gif" width="80" height="40" alt="MSI" title="MSI"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/nvidia-cc-3848.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/3848-s.gif" width="80" height="40" alt="NVIDIA" title="NVIDIA"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/phanteks-43-4600.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/4600-s.gif" width="80" height="40" alt="Phanteks" title="Phanteks"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/pulselabz-be-5461.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/5461-s.gif" width="80" height="40" alt="PulseLabZ" title="PulseLabZ"></a></li>
								
									
									<li><a href="https://www.ncix.com/vendor/qnap-inc-a6-3778.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/3778-s.gif" width="80" height="40" alt="QNAP Inc." title="QNAP Inc."></a></li>
								
							</ul>
							<div class="sub-category-holder" style="padding-top:5px;">
								<strong>Shop By Brands</strong>
								<div>
									<ul class="sub-category-list"  style="color: #717171;font-size:14px;">
										
										
										<li>
											<a href="https://www.ncix.com/vendor/adata-technology-19-3479.htm">AData Technology</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/asrock-70-3365.htm">ASRock</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/azio-corporation-24-4402.htm">AZIO Corporation</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/baseus-90-5265.htm">Baseus</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/bassworx-47-4716.htm">Bassworx</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/be-quiet-dc-4703.htm">be quiet!</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/beyerdynamic-bc-4719.htm">Beyerdynamic</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/bitfenix-c8-4371.htm">BitFenix</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/breo-6d-4873.htm">Breo</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/c2g-cables-to-go-54-3279.htm">C2G / CABLES TO GO</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/cablemod-74-5058.htm">CableMod</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ceomate-31-5227.htm">Ceomate</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/coolermaster-38-187.htm">COOLERMASTER</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/corsair-9e-135.htm">Corsair</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/cryorig-43-5318.htm">CRYORIG</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/d-link-30-90.htm">D-Link</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/dji-9e-5093.htm">DJI</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ducky-8a-4689.htm">Ducky</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ek-water-blocks-88-3730.htm">EK Water Blocks</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/electrohome-94-3784.htm">Electrohome</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/evga-eb-3465.htm">eVGA</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/fractal-design-4f-4259.htm">Fractal Design</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/general-brand-52-4522.htm">General Brand</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/gigabyte-fb-3.htm">Gigabyte</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/hipstreet-00-4541.htm">HIPSTREET</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/hp-printers-and-supplies-c8-14.htm">HP Printers and Supplies</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ibm-cf-5.htm">IBM</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/insta360-d4-5220.htm">Insta360</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/intel-55-28.htm">Intel</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ion-cables-dd-3704.htm">Ion Cables</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/kanto-b4-4884.htm">Kanto</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/kingston-e5-98.htm">Kingston</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/kp-water-50-5199.htm">KP Water</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/lexmark-5e-30.htm">Lexmark</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/lian-li-87-179.htm">LIAN-LI</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/linke-0d-4820.htm">Linke</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/linksys-90-119.htm">Linksys</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/liteon-7d-78.htm">Liteon</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/logitech-75-69.htm">Logitech</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/lucid-sound-80-5451.htm">Lucid Sound</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/mediasonic-e7-3469.htm">Mediasonic</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/microsoft-a7-4.htm">Microsoft</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/microsoft-oem-software-e2-3697.htm">Microsoft OEM Software</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/msi-e2-74.htm">MSI</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ncix-9c-85.htm">NCIX</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ncixpc-9b-3343.htm">NCIXPC</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/nextav-55-4598.htm">NextAV</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/ngear-technologies-inc-af-3307.htm">nGear Technologies Inc.</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/nvidia-cc-3848.htm">NVIDIA</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/nxbasics-a9-5051.htm">NXBasics</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/nxfusion-4b-5302.htm">NXFusion</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/nzxt-a3-3582.htm">NZXT</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/osd-7f-5458.htm">OSD</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/others-5b-11.htm">Others</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/peplink-21-4376.htm">Peplink</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/phanteks-43-4600.htm">Phanteks</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/qnap-inc-a6-3778.htm">QNAP Inc.</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/reeven-87-5449.htm">Reeven</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/rii-f6-4329.htm">Rii</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/robo-3d-7d-5316.htm">ROBO 3D</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/samsung-07-53.htm">Samsung</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/samsung-memory-storage-83-4611.htm">Samsung Memory & Storage</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/sapphire-4e-3358.htm">SAPPHIRE</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/seagate-61-8.htm">Seagate</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/silverstone-technology-3d-3422.htm">Silverstone Technology</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/startech-com-33-3458.htm">StarTech.com</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/sunny-clouds-c3-5237.htm">Sunny clouds</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/supermicro-9e-89.htm">SuperMicro</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/tesoro-a3-4955.htm">Tesoro</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/thermos-d1-5250.htm">Thermos</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/trendnet-bf-3304.htm">TRENDnet</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/unitek-5c-4168.htm">Unitek</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/visiontek-0e-3179.htm">VISIONTEK</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/wacaco-company-51-5352.htm">Wacaco Company</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/western-digital-wd-33-12.htm">Western Digital WD</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/whale-electronic-cookware-co-b2-5178.htm">Whale Electronic Cookware Co.</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/xerox-31-3050.htm">XEROX</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/xiaoyi-e2-5226.htm">Xiaoyi</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/zebra-technologies-4b-3268.htm">ZEBRA TECHNOLOGIES</a>
										</li>
										
										
										<li>
											<a href="https://www.ncix.com/vendor/zotac-14-4013.htm">Zotac</a>
										</li>
										
									</ul>
								</div>
							</div>
						</div>
						<div class="banner-holder">
							
							<!--Brands-->
<a href="https://www.ncix.com/search/?q=logitech" target="_blank">
<img src="https://dhsj95t7aazhx.cloudfront.net/eblast_ca031317/images/logitech_gaming_240x425.jpg" alt="Logitech Gaming Peripherals" width="240" height="425"></a>
							
						</div>
					</div>
				</li>
				<li>
					<a href="https://www.ncix.com/promotion/" alt="Weekly Sale" title="Weekly Sale">Weekly Sale</a>
					<div class="drop">
						<div class="deal-block">
						
							<style>
.deal-holder a
{
color:#B11D16;
}
.deal-holder a:hover
{
color:#C30;
}
.deal-holder
{
border-top: 0px;
padding: 0px 0px 0px;
}
</style>
<div class="deal-holder">
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/promotion/"><img src="/_img/ico-sale.jpg" alt="NCIX Weekly Sale" width="34" height="36"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/promotion/"><p class="text" style="font-size:14px;">WEEKLY SALE!</p></a></strong>
<p>Get great deals every week with our weekly sale. Starts 6pm PST every Wednesday!</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/subpromo/1382.htm"><img src="/_img/ico-deals.jpg" alt="NCIX WEEKEND DEALS" width="32" height="36"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/subpromo/1382.htm"><p class="text" style="font-size:14px;">WEEKEND DEALS</p></a></strong>
<p>End your week with some great technology deals, posted every Friday.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/clearance/"><img src="/_img/ico-store.jpg" alt="NCIX CLEARANCE CENTER" width="38" height="35"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/clearance/"><p class="text" style="font-size:14px;">CLEARANCE CENTER</p></a></strong>
<p>Discounts on clearance and end-of-life items!</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/openbox/"><img src="/_img/ico-refurbs.jpg" alt="Open Box and refurbs" width="37" height="33"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/openbox/">
<p class="text" style="font-size:14px;">OPEN BOX & REFURBS</p></a></strong>
<p>Save even more on returned, open box and refurbished products.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/newsletters/"><img src="/_img/ico-subscribe.jpg" alt="NCIX Subscribe and Win" width="37" height="24"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/newsletters/">
<p class="text" style="font-size:14px;">SUBSCRIBE & WIN</p></a></strong>
<p>Get email alerts on all our great deals and offers. Get a chance to win great prizes!</p>
</div>
</div>
<div class="deal-holder">
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/article/premier_partner.htm"><img src="/_img/ico-partner.jpg" alt="NCIX Premier Partner program" width="33" height="36"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/article/premier_partner.htm"><p class="text" style="font-size:14px;">PREMIER PARTNER</p></a></strong>
<p>Every day reseller pricing for just $149 a year.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/article/vip.htm"><img src="/_img/ico-members.jpg"alt="NCIX VIP Membership" width="37" height="29"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/article/vip.htm">
<p class="text" style="font-size:14px;">VIP MEMBERS</p></a></strong>
<p>Just $49 a year gets you free RMA, priority service and more!</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/supershippingsaverclub"><img src="/_img/ico-shipping.jpg" alt="Super Shipping Saver Club" width="37" height="27"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/supershippingsaverclub">
<p class="text" style="font-size:14px;">SUPER SHIPPING</p></a></strong>
<p>For $99 a year, get unlimited ground shipping on most orders over $50.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://stores.ebay.com/NCIX-Outlet-Store"><img src="/_img/ico-refurbs.jpg" alt="NCIX eBay Outlet Store" width="36" height="35"></a>
</div>
<strong class="title"><a href="https://stores.ebay.com/NCIX-Outlet-Store">
<p class="text" style="font-size:14px;">eBay Outlet Store</p></a></strong>
<p>Last chance to save on new or refurbished items. Listings refresh weekly.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/article/ncix-giftcards.htm"><img src="/_img/ico-gift.jpg" alt="NCIX Gift Cards" width="31" height="36"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/article/ncix-giftcards.htm">
<p class="text" style="font-size:14px;">NCIX GIFT CARDS</p></a></strong>
<p>Give the gift of awesome. NCIX Gift Cards never expire. A great gift for anyone!</p>
</div>
</div>

						</div>
						<div class="banner-holder">
							
							<iframe src="https://dhsj95t7aazhx.cloudfront.net/NCIX-Newsletter-Signup/index.html" width="480" height="425" frameborder="0" scrolling="no">
<p>Your browser does not support iframes.</p>
</iframe>
 
							
						</div>
					</div>
				</li>
				<li>
					<a href="https://www.ncix.com/article/NCIX-PC.htm#start">NCIX PC</a>
					<div class="drop">
						<div class="drop-holder">
							
							<!--
<div class="support-block"
style="width:811px; height:425px; background-image:url('https://dhsj95t7aazhx.cloudfront.net/NCIXPC/images/Villain-Tab_03.jpg?123456977'); cursor: pointer; background-repeat:no-repeat;"
onclick="location.href='https://www.ncix.com/article/NCIX-PC-Villain.htm';" >-->

<div class="support-block"
style="width:811px; height:425px; " >
<div class="column" style="cursor: pointer;" onclick="location.href='https://www.ncix.com/ncixpc_new/';">
<div class="icon-holder">
<a href="https://www.ncix.com/ncixpc_new/"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/dropdown_bnr/ncixpc-logo.png" alt="NCIX PC Logo" width="95"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/ncixpc_new/">NCIX PC</a></strong>
<p>Superior handcrafted desktops. We build yours like it was our own. </p>
</div>
<div class="column" style="cursor: pointer;" onclick="location.href='https://www.ncix.com/ncixpc_new/pcbuilderreconfig_new.cfm?id=10179';">
<div class="icon-holder">
<a href="https://www.ncix.com/ncixpc_new/pcbuilderreconfig_new.cfm?id=10179"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/dropdown_bnr/builder-icon.png?1" alt="NCIX PC Builder Wrench Screwdriver Logo" width="95"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/ncixpc_new/pcbuilderreconfig_new.cfm?id=10179">Design Studio</a></strong>
<p>You Dream It, We Build It. Customize yours now.</p>
</div>
</div>

							
						</div>
						<div class="banner-holder">
							
							<!--NCIX PC-->
<div style="width:100%; background-color:#000">
<a href="https://www.ncix.com/ncixpc_new/" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/dropdown_bnr/NCIX-Promo_240x425.jpg" border="0" display="block" alt="Shop Custom Gaming Desktops - The Ultimate Gaming Experience"/></a>
</div>
<!--
<div style="width:100%; background-color:#000">
<a href="https://www.ncix.com/article/NCIX-PC-Villain.htm" target="_blank"><img src="https://dhsj95t7aazhx.cloudfront.net/NCIXPC/images/Villain-Tab_04.jpg?338877" border="0" display="block" alt="Shop Custom Gaming Desktops - The Ultimate Gaming Experience"/></a>
</div-->
							
						</div>
					</div>
				</li>

				<li>
					<a href="https://www.ncix.com/techservices/"  alt="Tech Service" title="Tech Service">Tech Service</a>
					<div class="drop">
						<div class="drop-holder">
							
								<div class="support-block">
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/techservices/"><img src="/_img/ico-support.jpg" alt="NCIX Technical Services Icon" width="44" height="38"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/techservices/">NCIX Tech Services</a></strong>
<p>Have a technical issue with your stuff? We’re here to help.</p>
<!--
<p><strong>Current response time is about 5 minutes right now.</strong></p>
-->
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/contact/"><img src="/_img/ico-directory.jpg" alt="Store Locations Directory Icon" width="48" height="48"></a>
</div>
<strong class="title"><a href="https://www.ncix.com/contact/">Store Locations</a></strong>
<p>Looking for our sales team, where our stores are located, and other contacts at NCIX?</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://secure1.ncix.com/message/"><img src="/_img/ico-message.jpg" alt="NCIX Support Team Icon" width="48" height="42"></a>
</div>
<strong class="title"><a href="https://secure1.ncix.com/message/">Send a Support Message</a></strong>
<p>The fastest way to reach our customer care team. Each messsage is carefully tracked until any issue is resolved.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://secure1.ncix.com/customersupport/"><img src="/_img/ico-track.jpg" alt="Order Tracking Icon" width="48" height="48"></a>
</div>
<strong class="title"><a href="https://secure1.ncix.com/customersupport/">Track Your Order</a></strong>
<p>Find out where your order is and approximately when it’ll arrive.</p>
</div>
</div>

						</div>
						<div class="banner-holder">
							
							<a href="https://www.ncix.com/techservices/">
<img src="https://dhsj95t7aazhx.cloudfront.net/NCIX-Tech-Services/NCIX-TrustBlue-21_240x425.jpg" alt="NCIX Tech Service" width="240" height="425"></a>
							
						</div>
					</div>
				</li>
				
				<li>
					<a href="https://www.ncix.com/forums/" alt="Forums" title="Forums">Forums</a>
					<div class="drop">
						<div class="drop-holder">
							
							<style>
.learn-block a
{
color:#B11D16;
}
.learn-block a:hover
{
color:#C30;
}
</style>
<div class="learn-block">
<div class="learn-holder">
<strong class="title">NCIX Communities</strong>
<div class="learn-frame">
<div class="column">
<div class="icon-holder">
<a href="https://forums.ncix.com/"><img src="/_img/ico-forums.jpg" alt="NCIX Forums" width="48" height="46"></a>
</div>
<strong class="sub-title"><a href="https://forums.ncix.com/">
<p class="text" style="font-size:14px;color:black;"><b>NCIX Forums</b></p></a></strong>
<p>Virtually any topic is discussed here.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.ncix.com/newsletters/"><img src="/_img/ico-promos.jpg"
alt="Promos and Sweepstakes" width="45" height="49"></a>
</div>
<strong class="sub-title"><a href="https://www.ncix.com/newsletters/">
<p class="text" style="font-size:14px;color:black;"><b>Promos & Sweepstakes</b></p></a></strong>
<p>Join the fun and get a chance to win great prizes.</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://forums.ncix.com/forums/?mode=section&forum=213"><img src="/_img/ico-team.jpg" alt="NCIX Folding Team" width="48" height="48"></a>
</div>
<strong class="sub-title"><a href="https://forums.ncix.com/forums/?mode=section&forum=213">
<p class="text" style="font-size:14px;color:black;"><b>NCIX Folding Team</b></p></a></strong>
<p>Folding @home helps research and charities.</p>
</div>
</div>
</div>
<div class="learn-holder">
<strong class="title">Featured</strong>
<div class="learn-frame">
<div class="column">
<div class="icon-holder">
<a href="https://bit.ly/1tmH4GM"><img src="/_img/ico-tutorials.jpg"
alt="NCIX Tech Tutorials" width="50" height="32"></a>
</div>
<strong class="sub-title"><a href="https://bit.ly/1tmH4GM">
<p class="text" style="font-size:14px;color:black;"><b>Tutorials</b></p></a></strong>
<p>Learn about the technology we sell. </p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://www.youtube.com/user/NCIXcom"><img src="/_img/ico-video.jpg" alt="NCIX Video Channels" width="50" height="49"></a>
</div>
<strong class="sub-title"><a href="https://www.youtube.com/user/NCIXcom">
<p class="text" style="font-size:14px;color:black;"><b>Video Channels</b></p></a></strong>
<p>Watch tutorials, unboxings, tech news and more!</p>
</div>
<div class="column">
<div class="icon-holder">
<a href="https://technews.ncix.com/"><img src="/_img/ico-reviews.jpg" alt="NCIX Blogs and Reviews" width="48" height="48"></a>
</div>
<strong class="sub-title"><a href="https://technews.ncix.com/">
<p class="text" style="font-size:14px;color:black;"><b>Blogs & Reviews</b></p></a></strong>
<p>Read insightful blogs on the latest tech products.</p>
</div>
</div>
</div></div>
							
						</div>
						<div class="banner-holder">
							
							<!-- Newsletter Subscribes -->
<a href="https://www.ncix.com/newsletters/">
<img src="https://dhsj95t7aazhx.cloudfront.net/SW1117DEP2.jpg" alt="Subscribe to our newsletter and Win!" width="240" height="425"></a>

							
						</div>
					</div>
				</li>
<li style="background:none !important;">
<a href="https://www.ncix.com/newsletters/"  alt="Newsletter" title="Newsletter">Newsletter</a>
</li>
<li style="background:none !important;">
<a href="https://www.ncix.com/business/"  alt="Business Center" title="Business Center">Business Center</a>
</li>


<li style="background:none !important;">
<a href="https://secure1.ncix.com/rewardcenter/" rel="nofollow" alt="Rewards Center" title="Rewards Center">Rewards Center</a>
</li>
 
<li style="background:none !important;">
<a href="https://www.ncix.com/contact/" alt="Store Locations" title="Store Locations">Store Locations</a>
</li>

			</ul>
		</nav>
</div>


	
		<table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF" >
			<tr valign="top">
				
				<td width="167" valign="top"  class="sm-left">
					






	






	




	
		
		





					


		

	



<style>
#nav-drop {
    position: relative;
    float: left;
    width: 148px;
}
.sidenav {
    font-size: 13px;
    line-height: 15px;
    background: #f6f6f6;
    font-weight: 700;
    position: relative;
    overflow: hidden;
    margin: 0;
    padding: 0;
    list-style: none;
}
.sidenav li {
    position: relative;
    border-bottom: 1px solid #bbb;
	background-repeat: no-repeat;
    background-position: right ;
	background-image: url('https://source.ncix.com/menu/arrow4b.png');
}
.sidenav a {
    padding: 7px 5px;
    display: block;
    color: #000;
}
.sidenav li:hover {
	background-color: #ccc;
}
</style>




	
	
		
	
	
			
			
	

<div id="spacing_6"></div>
<div id="menu">
	

		<div style="background-color:#f2f8ff;">
			
			
			
			<div><span class="headline" style="color:#0054a6;; padding-left:3px;">DDR3 Memory</span></div>
			
				<div style=" padding-left:5px;padding-top:10px;"><span class="headline" style="color:#000;">Size</span></div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="906" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-12gb-84-1303-906.htm" ><span  class="sub_link" id="subcategoryname906">12GB</span></a><span class="qtycount"> (3)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="1022" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-16gb-a2-1303-1022.htm" ><span  class="sub_link" id="subcategoryname1022">16GB</span></a><span class="qtycount"> (19)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="481" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-2gb-92-1303-481.htm" ><span  class="sub_link" id="subcategoryname481">2GB</span></a><span class="qtycount"> (2)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="1385" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-32gb-c9-1303-1385.htm" ><span  class="sub_link" id="subcategoryname1385">32GB</span></a><span class="qtycount"> (2)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="482" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-4gb-41-1303-482.htm" ><span  class="sub_link" id="subcategoryname482">4GB</span></a><span class="qtycount"> (13)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="999" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-8gb-6b-1303-999.htm" ><span  class="sub_link" id="subcategoryname999">8GB</span></a><span class="qtycount"> (26)</span>
					</div>
				
			
				<div style=" padding-left:5px;padding-top:10px;"><span class="headline" style="color:#000;">Speed</span></div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="474" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-ddr3-1333-3f-1303-474.htm" ><span  class="sub_link" id="subcategoryname474">DDR3-1333</span></a><span class="qtycount"> (12)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="475" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-ddr3-1600-d8-1303-475.htm" ><span  class="sub_link" id="subcategoryname475">DDR3-1600</span></a><span class="qtycount"> (38)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="477" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-ddr3-1866-68-1303-477.htm" ><span  class="sub_link" id="subcategoryname477">DDR3-1866</span></a><span class="qtycount"> (11)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="530" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-ddr3-2133-d1-1303-530.htm" ><span  class="sub_link" id="subcategoryname530">DDR3-2133</span></a><span class="qtycount"> (2)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="1097" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-ddr3-2400-56-1303-1097.htm" ><span  class="sub_link" id="subcategoryname1097">DDR3-2400</span></a><span class="qtycount"> (1)</span>
					</div>
				
			
				<div style=" padding-left:5px;padding-top:10px;"><span class="headline" style="color:#000;">Configuration</span></div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="478" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-dual-channel-f8-1303-478.htm" ><span  class="sub_link" id="subcategoryname478">Dual Channel</span></a><span class="qtycount"> (25)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="1413" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-quad-channel-44-1303-1413.htm" ><span  class="sub_link" id="subcategoryname1413">Quad Channel</span></a><span class="qtycount"> (2)</span>
					</div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="895" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-triple-channel-76-1303-895.htm" ><span  class="sub_link" id="subcategoryname895">Triple Channel</span></a><span class="qtycount"> (2)</span>
					</div>
				
			
				<div style=" padding-left:5px;padding-top:10px;"><span class="headline" style="color:#000;">Others</span></div>
				
					
					<div class="submenu_cats" id="s1303" style="padding:0px; padding-left:6px">
						
						<input type="checkbox"  style="padding-left:10px" name="productsmid" value="484" onclick="changeweight($(this))"/>
						<a href="https://www.ncix.com/category/ddr3-memory-xmp-42-1303-484.htm" ><span  class="sub_link" id="subcategoryname484">XMP</span></a><span class="qtycount"> (9)</span>
					</div>
				
			
			<div style="padding:10px 3px;">
				<input type="button" name="filter" value="Filter"   class="filterBtn" onclick="FilterProductList(1303)" />
			</div>
			
				
					
					<div id="submenu_title_related">
						<span class="headline">
							
								<img id="a1297" src="https://d1sfu4378rr01a.cloudfront.net/_img/plus.gif" align="absbottom" style="cursor:pointer" onClick="moreoption('1297')" border="0"><a href="https://www.ncix.com/category/ddr-desktop-memory-6f-1297.htm" class="sub_link">DDR Desktop Memory</a>
							
						</span>
					</div>
					
						<div class="submenu_cats" style="display:none" id="s1297">
						
							
							<a href="https://www.ncix.com/category/ddr-desktop-memory-pc2700-ea-1297-404.htm" class="sub_link"  style="padding-left:10px">PC2700</span></a><span class="qtycount"> (1)</span><br />
						
						</div>
					
			
					
					<div id="submenu_title_related">
						<span class="headline">
							
								<img id="a1300" src="https://d1sfu4378rr01a.cloudfront.net/_img/plus.gif" align="absbottom" style="cursor:pointer" onClick="moreoption('1300')" border="0"><a href="https://www.ncix.com/category/ddr2-desktop-memory-25-1300.htm" class="sub_link">DDR2 Desktop Memory</a>
							
						</span>
					</div>
					
						<div class="submenu_cats" style="display:none" id="s1300">
						
							
							<a href="https://www.ncix.com/category/ddr2-desktop-memory-2gb-e1-1300-444.htm" class="sub_link"  style="padding-left:10px">2GB</span></a><span class="qtycount"> (1)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr2-desktop-memory-4gb-56-1300-445.htm" class="sub_link"  style="padding-left:10px">4GB</span></a><span class="qtycount"> (1)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr2-desktop-memory-pc2-6400-57-1300-435.htm" class="sub_link"  style="padding-left:10px">PC2-6400</span></a><span class="qtycount"> (2)</span><br />
						
						</div>
					
			
					
					<div id="submenu_title_related">
						<span class="headline">
							
								<img id="a1344" src="https://d1sfu4378rr01a.cloudfront.net/_img/plus.gif" align="absbottom" style="cursor:pointer" onClick="moreoption('1344')" border="0"><a href="https://www.ncix.com/category/ddr3-server-ram-c7-1344.htm" class="sub_link">DDR3 Server RAM</a>
							
						</span>
					</div>
					
						<div class="submenu_cats" style="display:none" id="s1344">
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-16gb-4e-1344-1389.htm" class="sub_link"  style="padding-left:10px">16GB</span></a><span class="qtycount"> (20)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-2gb-c9-1344-990.htm" class="sub_link"  style="padding-left:10px">2GB</span></a><span class="qtycount"> (4)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-32gb-f8-1344-1506.htm" class="sub_link"  style="padding-left:10px">32GB</span></a><span class="qtycount"> (2)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-48gb-59-1344-1390.htm" class="sub_link"  style="padding-left:10px">48GB</span></a><span class="qtycount"> (3)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-4gb-62-1344-1467.htm" class="sub_link"  style="padding-left:10px">4GB</span></a><span class="qtycount"> (8)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-6gb-3e-1344-1388.htm" class="sub_link"  style="padding-left:10px">6GB</span></a><span class="qtycount"> (2)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-8gb-44-1344-1354.htm" class="sub_link"  style="padding-left:10px">8GB</span></a><span class="qtycount"> (23)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-ddr3-1066-85-1344-975.htm" class="sub_link"  style="padding-left:10px">DDR3-1066</span></a><span class="qtycount"> (10)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-ddr3-1333-c6-1344-974.htm" class="sub_link"  style="padding-left:10px">DDR3-1333</span></a><span class="qtycount"> (25)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-ddr3-1600-e1-1344-1469.htm" class="sub_link"  style="padding-left:10px">DDR3-1600</span></a><span class="qtycount"> (26)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-ddr3-1866-2c-1344-1769.htm" class="sub_link"  style="padding-left:10px">DDR3-1866</span></a><span class="qtycount"> (1)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-ecc-3e-1344-989.htm" class="sub_link"  style="padding-left:10px">ECC</span></a><span class="qtycount"> (62)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-intel-compatibility-tested-51-1344-1436.htm" class="sub_link"  style="padding-left:10px">Intel Compatibility Tested</span></a><span class="qtycount"> (4)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-quad-channel-0f-1344-1439.htm" class="sub_link"  style="padding-left:10px">Quad Channel</span></a><span class="qtycount"> (10)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-registered-6e-1344-1103.htm" class="sub_link"  style="padding-left:10px">Registered</span></a><span class="qtycount"> (45)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-thermal-sensor-b6-1344-1468.htm" class="sub_link"  style="padding-left:10px">Thermal Sensor</span></a><span class="qtycount"> (6)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-server-ram-triple-channel-b6-1344-1438.htm" class="sub_link"  style="padding-left:10px">Triple Channel</span></a><span class="qtycount"> (2)</span><br />
						
						</div>
					
			
					
					<div id="submenu_title_related">
						<span class="headline">
							
								<img id="a1319" src="https://d1sfu4378rr01a.cloudfront.net/_img/plus.gif" align="absbottom" style="cursor:pointer" onClick="moreoption('1319')" border="0"><a href="https://www.ncix.com/category/ddr3-sodimm-ram-19-1319.htm" class="sub_link">DDR3 SODIMM RAM</a>
							
						</span>
					</div>
					
						<div class="submenu_cats" style="display:none" id="s1319">
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-16gb-90-1319-1456.htm" class="sub_link"  style="padding-left:10px">16GB</span></a><span class="qtycount"> (6)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-2gb-26-1319-1046.htm" class="sub_link"  style="padding-left:10px">2GB</span></a><span class="qtycount"> (3)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-4gb-c5-1319-1047.htm" class="sub_link"  style="padding-left:10px">4GB</span></a><span class="qtycount"> (5)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-8gb-18-1319-1048.htm" class="sub_link"  style="padding-left:10px">8GB</span></a><span class="qtycount"> (15)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-ddr3-1066-f7-1319-566.htm" class="sub_link"  style="padding-left:10px">DDR3-1066</span></a><span class="qtycount"> (2)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-ddr3-1333-19-1319-565.htm" class="sub_link"  style="padding-left:10px">DDR3-1333</span></a><span class="qtycount"> (7)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-ddr3-1600-54-1319-1457.htm" class="sub_link"  style="padding-left:10px">DDR3-1600</span></a><span class="qtycount"> (19)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-ddr3-1866-4d-1319-1472.htm" class="sub_link"  style="padding-left:10px">DDR3-1866</span></a><span class="qtycount"> (2)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-ddr3-2133-db-1319-1543.htm" class="sub_link"  style="padding-left:10px">DDR3-2133</span></a><span class="qtycount"> (3)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr3-sodimm-ram-dual-channel-b8-1319-1473.htm" class="sub_link"  style="padding-left:10px">Dual Channel</span></a><span class="qtycount"> (9)</span><br />
						
						</div>
					
			
					
					<div id="submenu_title_related">
						<span class="headline">
							
								<img id="a1516" src="https://d1sfu4378rr01a.cloudfront.net/_img/plus.gif" align="absbottom" style="cursor:pointer" onClick="moreoption('1516')" border="0"><a href="https://www.ncix.com/category/ddr4-memory-27-1516.htm" class="sub_link">DDR4 Memory</a>
							
						</span>
					</div>
					
						<div class="submenu_cats" style="display:none" id="s1516">
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-1-2v-b5-1516-2040.htm" class="sub_link"  style="padding-left:10px">1.2V</span></a><span class="qtycount"> (111)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-1-35v-71-1516-2042.htm" class="sub_link"  style="padding-left:10px">1.35V</span></a><span class="qtycount"> (115)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-128gb-ca-1516-1927.htm" class="sub_link"  style="padding-left:10px">128GB</span></a><span class="qtycount"> (3)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-16gb-e1-1516-1783.htm" class="sub_link"  style="padding-left:10px">16GB</span></a><span class="qtycount"> (85)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-32gb-af-1516-1784.htm" class="sub_link"  style="padding-left:10px">32GB</span></a><span class="qtycount"> (76)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-4gb-e0-1516-2222.htm" class="sub_link"  style="padding-left:10px">4GB</span></a><span class="qtycount"> (7)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-64gb-f2-1516-2053.htm" class="sub_link"  style="padding-left:10px">64GB</span></a><span class="qtycount"> (36)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-8gb-ae-1516-2039.htm" class="sub_link"  style="padding-left:10px">8GB</span></a><span class="qtycount"> (40)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr-3400-23-1516-2050.htm" class="sub_link"  style="padding-left:10px">DDR-3400</span></a><span class="qtycount"> (2)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-2133-d2-1516-1778.htm" class="sub_link"  style="padding-left:10px">DDR4-2133</span></a><span class="qtycount"> (34)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-2400-23-1516-1779.htm" class="sub_link"  style="padding-left:10px">DDR4-2400</span></a><span class="qtycount"> (53)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-2666-2b-1516-1780.htm" class="sub_link"  style="padding-left:10px">DDR4-2666</span></a><span class="qtycount"> (39)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-2800-1c-1516-1781.htm" class="sub_link"  style="padding-left:10px">DDR4-2800</span></a><span class="qtycount"> (12)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-3000-8f-1516-1782.htm" class="sub_link"  style="padding-left:10px">DDR4-3000</span></a><span class="qtycount"> (31)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-3200-1e-1516-1785.htm" class="sub_link"  style="padding-left:10px">DDR4-3200</span></a><span class="qtycount"> (40)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-3333-f3-1516-2044.htm" class="sub_link"  style="padding-left:10px">DDR4-3333</span></a><span class="qtycount"> (6)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-3466-a5-1516-2051.htm" class="sub_link"  style="padding-left:10px">DDR4-3466</span></a><span class="qtycount"> (8)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-3600-14-1516-2052.htm" class="sub_link"  style="padding-left:10px">DDR4-3600</span></a><span class="qtycount"> (22)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-3866-e3-1516-2362.htm" class="sub_link"  style="padding-left:10px">DDR4-3866</span></a><span class="qtycount"> (1)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-4000-76-1516-2318.htm" class="sub_link"  style="padding-left:10px">DDR4-4000</span></a><span class="qtycount"> (2)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-ddr4-4266-f7-1516-2364.htm" class="sub_link"  style="padding-left:10px">DDR4-4266</span></a><span class="qtycount"> (1)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-dual-channel-8a-1516-1776.htm" class="sub_link"  style="padding-left:10px">Dual Channel</span></a><span class="qtycount"> (105)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-octa-channel-b3-1516-1928.htm" class="sub_link"  style="padding-left:10px">Octa Channel</span></a><span class="qtycount"> (3)</span><br />
						
							
							<a href="https://www.ncix.com/category/ddr4-memory-quad-channel-21-1516-1777.htm" class="sub_link"  style="padding-left:10px">Quad Channel</span></a><span class="qtycount"> (97)</span><br />
						
						</div>
					
			
					
					<div id="submenu_title_related">
						<span class="headline">
							
								<img src="https://d1sfu4378rr01a.cloudfront.net/images/space.gif" align="absbottom" width="16"><a href="https://www.ncix.com/category/desktop-sdram-f2-1304.htm" class="sub_link">Desktop SDRAM</a>
							
						</span>
					</div>
					
			
					
					<div id="submenu_title_related">
						<span class="headline">
							
								<img id="a107" src="https://d1sfu4378rr01a.cloudfront.net/_img/plus.gif" align="absbottom" style="cursor:pointer" onClick="moreoption('107')" border="0"><a href="https://www.ncix.com/category/motherboards-90-107.htm" class="sub_link">Motherboards</a>
							
						</span>
					</div>
					
						<div class="submenu_cats" style="display:none" id="s107">
						
							
							<a href="https://www.ncix.com/category/motherboards-am4-f0-107-2389.htm" class="sub_link"  style="padding-left:10px">AM4</span></a><span class="qtycount"> (57)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-amd-a320-3c-107-2392.htm" class="sub_link"  style="padding-left:10px">AMD A320</span></a><span class="qtycount"> (11)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-amd-b350-12-107-2391.htm" class="sub_link"  style="padding-left:10px">AMD B350</span></a><span class="qtycount"> (25)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-amd-x370-46-107-2390.htm" class="sub_link"  style="padding-left:10px">AMD X370</span></a><span class="qtycount"> (18)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-amd-x399-44-107-2450.htm" class="sub_link"  style="padding-left:10px">AMD X399</span></a><span class="qtycount"> (5)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-atx-bd-107-13.htm" class="sub_link"  style="padding-left:10px">ATX</span></a><span class="qtycount"> (112)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-embedded-cpu-e1-107-1369.htm" class="sub_link"  style="padding-left:10px">Embedded CPU</span></a><span class="qtycount"> (7)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-extended-atx-93-107-112.htm" class="sub_link"  style="padding-left:10px">Extended ATX</span></a><span class="qtycount"> (12)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-fm2-db-107-1525.htm" class="sub_link"  style="padding-left:10px">FM2+</span></a><span class="qtycount"> (9)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-b250-e2-107-2360.htm" class="sub_link"  style="padding-left:10px">Intel B250</span></a><span class="qtycount"> (15)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-b85-b2-107-904.htm" class="sub_link"  style="padding-left:10px">Intel B85</span></a><span class="qtycount"> (3)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-h270-2d-107-2359.htm" class="sub_link"  style="padding-left:10px">Intel H270</span></a><span class="qtycount"> (7)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-h81-a4-107-7.htm" class="sub_link"  style="padding-left:10px">Intel H81</span></a><span class="qtycount"> (6)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-q87-94-107-201.htm" class="sub_link"  style="padding-left:10px">Intel Q87</span></a><span class="qtycount"> (1)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-x299-05-107-2433.htm" class="sub_link"  style="padding-left:10px">Intel X299</span></a><span class="qtycount"> (16)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-x99-17-107-902.htm" class="sub_link"  style="padding-left:10px">Intel X99</span></a><span class="qtycount"> (8)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-z170-9e-107-122.htm" class="sub_link"  style="padding-left:10px">Intel Z170</span></a><span class="qtycount"> (6)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-z270-65-107-2358.htm" class="sub_link"  style="padding-left:10px">Intel Z270</span></a><span class="qtycount"> (22)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-intel-z370-70-107-2459.htm" class="sub_link"  style="padding-left:10px">Intel Z370</span></a><span class="qtycount"> (26)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-lga-1150-fb-107-1632.htm" class="sub_link"  style="padding-left:10px">LGA 1150</span></a><span class="qtycount"> (12)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-lga-1151-82-107-2049.htm" class="sub_link"  style="padding-left:10px">LGA 1151</span></a><span class="qtycount"> (114)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-lga-2011-bf-107-1412.htm" class="sub_link"  style="padding-left:10px">LGA 2011</span></a><span class="qtycount"> (5)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-lga-2011-v3-57-107-27.htm" class="sub_link"  style="padding-left:10px">LGA 2011-v3</span></a><span class="qtycount"> (8)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-lga-2066-a6-107-2408.htm" class="sub_link"  style="padding-left:10px">LGA 2066</span></a><span class="qtycount"> (20)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-micro-atx-21-107-1107.htm" class="sub_link"  style="padding-left:10px">Micro-ATX</span></a><span class="qtycount"> (71)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-mini-itx-65-107-891.htm" class="sub_link"  style="padding-left:10px">Mini-ITX</span></a><span class="qtycount"> (24)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-sli-ready-28-107-132.htm" class="sub_link"  style="padding-left:10px">SLI Ready</span></a><span class="qtycount"> (64)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-tr4-63-107-2451.htm" class="sub_link"  style="padding-left:10px">TR4</span></a><span class="qtycount"> (6)</span><br />
						
							
							<a href="https://www.ncix.com/category/motherboards-usb-3-1-bc-107-1844.htm" class="sub_link"  style="padding-left:10px">USB 3.1</span></a><span class="qtycount"> (133)</span><br />
						
						</div>
					
			
		


		</div>
	

	<div id="sublinks">
		
		
		
		
			
		      <a href="https://www.ncix.com/category/adapters-b0-1256.htm" class="sub_link">Adapters </span></a><span class="qtycount"><span class="qtycount"> (176)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/bundle-deals-75-1265.htm" class="sub_link">Bundle Deals</span></a><span class="qtycount"><span class="qtycount"> (122)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/cables-f7-1168.htm" class="sub_link">Cables </span></a><span class="qtycount"><span class="qtycount"> (1805)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/computer-cases-53-104.htm" class="sub_link">Computer Cases</span></a><span class="qtycount"><span class="qtycount"> (462)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/computer-speakers-57-103.htm" class="sub_link">Computer Speakers</span></a><span class="qtycount"><span class="qtycount"> (24)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/cpus-processors-0b-106.htm" class="sub_link">CPUs / Processors</span></a><span class="qtycount"><span class="qtycount"> (237)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/data-projectors-15-1228.htm" class="sub_link">Data Projectors</span></a><span class="qtycount"><span class="qtycount"> (106)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/ddr3-memory-d0-1303.htm" class="sub_link">DDR3 Memory</span></a><span class="qtycount"><span class="qtycount"> (126)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/ddr4-memory-27-1516.htm" class="sub_link">DDR4 Memory</span></a><span class="qtycount"><span class="qtycount"> (285)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/external-hard-drives-ca-1272.htm" class="sub_link">External Hard Drives</span></a><span class="qtycount"><span class="qtycount"> (153)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/hard-drives-d6-109.htm" class="sub_link">Hard Drives</span></a><span class="qtycount"><span class="qtycount"> (335)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/home-automation-99-1337.htm" class="sub_link">Home Automation</span></a><span class="qtycount"><span class="qtycount"> (22)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/keyboards-1b-101.htm" class="sub_link">Keyboards</span></a><span class="qtycount"><span class="qtycount"> (352)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/laser-printers-8a-1032.htm" class="sub_link">Laser Printers</span></a><span class="qtycount"><span class="qtycount"> (98)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/lcd-monitors-69-1003.htm" class="sub_link">LCD Monitors</span></a><span class="qtycount"><span class="qtycount"> (364)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/media-players-71-1331.htm" class="sub_link">Media Players</span></a><span class="qtycount"><span class="qtycount"> (40)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/mice-35-102.htm" class="sub_link">Mice</span></a><span class="qtycount"><span class="qtycount"> (291)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/motherboards-90-107.htm" class="sub_link">Motherboards</span></a><span class="qtycount"><span class="qtycount"> (429)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/network-adapters-f9-1004.htm" class="sub_link">Network Adapters</span></a><span class="qtycount"><span class="qtycount"> (271)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/network-storage-nas-8c-1191.htm" class="sub_link">Network Storage NAS</span></a><span class="qtycount"><span class="qtycount"> (293)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/network-switches-79-1005.htm" class="sub_link">Network Switches</span></a><span class="qtycount"><span class="qtycount"> (469)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/operating-systems-22-1055.htm" class="sub_link">Operating Systems</span></a><span class="qtycount"><span class="qtycount"> (46)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/power-supplies-74-1066.htm" class="sub_link">Power Supplies</span></a><span class="qtycount"><span class="qtycount"> (291)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/solid-state-drive-ssd-be-1275.htm" class="sub_link">Solid State Drive - SSD</span></a><span class="qtycount"><span class="qtycount"> (254)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/surveillance-systems-f9-1313.htm" class="sub_link">Surveillance Systems</span></a><span class="qtycount"><span class="qtycount"> (35)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/tablets-77-1384.htm" class="sub_link">Tablets</span></a><span class="qtycount"><span class="qtycount"> (113)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/unlocked-smartphones-28-1216.htm" class="sub_link">Unlocked Smartphones</span></a><span class="qtycount"><span class="qtycount"> (109)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/video-cards-72-108.htm" class="sub_link">Video Cards</span></a><span class="qtycount"><span class="qtycount"> (258)</span><br />
		 
			
		      <a href="https://www.ncix.com/category/wireless-wifi-routers-3d-1046.htm" class="sub_link">Wireless (WiFi) Routers </span></a><span class="qtycount"><span class="qtycount"> (133)</span><br />
		 
		 
    </div>
</div>
 <script language="JavaScript">
 	function moreoption(categoryid)
	{
		imgobj = document.getElementById('a'+categoryid);

		if(imgobj.src != "" && imgobj.src.indexOf('minus.gif') > 0 )
		{
			imgobj.src	=	"/_img/plus.gif";
		}else{
			imgobj.src="/_img/minus.gif";
		}
		subobj = document.getElementById('s'+categoryid);
		subobj.style.display	=	subobj.style.display=="none"?"":"none";
	}

	function changeweight(obj)
	{
		var o	=	$("#subcategoryname" +obj.val());
		if(o.hasClass("fontbold"))
			{o.removeClass("fontbold");}
		else
			{o.addClass("fontbold");}
	}
 </script>
 
 <div style="margin:10px; text-align:right"><strong><a href="https://www.ncix.com/categories/"><font size="1">&raquo;&nbsp;More&nbsp;Categories</font></a></strong></div>


<style>
	.fontbold{font-weight:bold;}
</style>

	

					






	






	




	
		
		





	
	
	


	
	

	
		
			
	

	
	
	


	
	

	
		
			
	

					
<style>
#speechbubble {position:relative; border:1px solid #999999;}
.tbox {font-family:Georgia, "Times New Roman", Times, serif; font-size:12px; font-weight:bold;}
.testimonial_text { font-family:Georgia, "Times New Roman", Times, serif; font-size:12px; line-height:19px; color:#454545;}
.username_text { font-family:Verdana, Geneva, sans-serif, Times, serif; font-size:12px; color:#000000;}
.username_texttwo { font-family:Verdana, Geneva, sans-serif, Times, serif; font-size:11px; line-height:16px; color:#0054a6; text-decoration:underline;} 
.testimonial_link { font-family:Verdana, Geneva, sans-serif; font-size:11px;}
</style>
<div align="center" style="margin-top:5px;padding-left:1px;">

    <table width="100%" cellpadding="0" cellspacing="2" border="0" id="speechbubble">
    <tr><td align="center" height="20"><span class="tbox">Testimonial Box</span></td></tr>
    <tr><td> 
        
        <table cellpadding="4" cellspacing="2">
        <tr><td>
        <span class="testimonial_text">
        
		"I would like to thank you guys for the amazing service and quality I have recieved as a customer. Responses ..."
        </span>
        </td></tr>
        </table>
        
	</td></tr>
	<tr><td align="right">
        <span class="username_text">
        &mdash; Trenton
        </span>
    </td></tr>
    <tr><td align="left">
        <a href="/testimonial/" class="username_texttwo">Read More</a></span><br />
        <a href="https://secure1.ncix.com/message/?dept=6" class="username_texttwo">Write Review</a></span><br />
    </td></tr>
    </table>
</div>

				</td>
				
				<td width="99%" class="normal" valign="top" style="padding:0px 10px;"> 
					
						



<div id="fpcalloutdiv" align="center" class="promocallout" style="font-size: 14px; font-weight: bold; color: #CC0000; margin-bottom: 5px;">&nbsp;</div>
<script type="text/javascript">
	$.getJSON("https://www.ncix.com/ajax/fpcallout.php?jsoncallback=?&r="+Date());
</script>
					
					
					
						






	






	




	
		
		





	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
	


	
	

	
		
			
	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
		
	


	
	

	
		
		
			
				
					
						<!--biz_memory_top-->
					
					<span style="display:none">Contentname:biz_memory_top</span>
							
			
			
	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
			
			
						
			
		
		
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
			
			
						
			
		
		
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
				
			
				
						
		
		
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	
		
			
				
						
		
		
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
				
						
		
		
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
				
			
				
						
		
		
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

					
					
						

<table cellpadding="0" cellspacing="0" width=100% align="center">
	<tr>
		<td style="text-align:left">
			
				
			
				






	






	




	
		
		





				
					
<div id="productlist">




	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	
	
	

	

	
	
	
	
	
	
	
	

	

	

	

	
	
	
	
	
	
	

	
	
	
	
	
	
	
	

















	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	


	
	
	
	
	


	
	
	
	
	
	
	

	




















	













<div id="breadcrumb">
	<ul class="bread-crumbs">
		<li class="crumb1">
			<div itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
			<a href="https://www.ncix.com/" title="Home" itemprop="url"><span itemprop="title">Home</span></a> &raquo;
			</div>
		</li>
		
		<li class="crumb2">
			
					<li class="crumb2"><div itemscope itemtype="http://data-vocabulary.org/Breadcrumb"><a href="http://www.ncix.com/computer-hardware/" title="computer-hardware" itemprop="url"><span itemprop="title">Computer Hardware</span></a> &raquo;</div></li>
				

		</li>
		<li class="crumb3">
			<div itemscope itemtype="http://data-vocabulary.org/Breadcrumb">
				<a href="https://www.ncix.com/majorcategory/memory-ddr3-0d-145.htm" title="Memory - DDR3" itemprop="url">
					<span itemprop="title">Memory - DDR3</span>
				</a>  &raquo;
			</div>
		</li>
		
			<li>
				DDR3 Memory
			</li>
		



		
	</ul>
</div>
<div style="clear:both"></div>
<h1>DDR3 Memory</h1>


	
	<br>

<table border='0' cellpadding='0' cellspacing='0' width='98%' class="normal">
	<tr>
		<td align="left"><font size="2"><b>Featured Products: <font color="red"> DDR3 Memory Deals</font></b></font></td>
	</tr>
</table>
<table width="98%" border="0" cellpadding="3" cellspacing="0" class="normal" style="border-collapse:collapse; margin-top:3px">
	
		
		
		
		
		
		
		
			
			
		
		
		
		

		

		

		

		
			<tr valign="top">
		
			<td width="33%" valign="top"  style="border-bottom:1px #e8e8e8 solid;border-right:1px #e8e8e8 solid;">
				<div style="padding:10px">
					<div>
							<div style="float:left; width:70%;text-align:center">
								<A class="normal" href="https://www.ncix.com/detail/corsair-vengeance-black-cmz16gx3m2a1600c10-16gb-d3-66354.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/images/66354_l.jpg" border="0" style="width:80%;height:auto; max-width:100%"  alt="Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit" title="Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit"></a>
							</div>
							<div style="float:right;width:30%;padding-top:20px;">
								
								
									<A href="https://www.ncix.com/vendor/corsair-9e-135.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/135-s.gif" border="0" width="80" height="40" alt="Corsair" title="Corsair"></a>
								
							</div>
					</div>
					<div style="clear:both; text-align:left; padding-top:12px;">
						<A title="SKU: 66354&#10;Mfr part #: CMZ16GX3M2A1600C10" href="https://www.ncix.com/detail/corsair-vengeance-black-cmz16gx3m2a1600c10-16gb-d3-66354.htm" style="font-size:1.2em">Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit</A>

					</div>
					<div style="clear:both;margin-top:5px; text-align:left; ">
						
								
								
								<strong>Price:&nbsp;</strong>
								<FONT color="#cc3300" size="2"><b>$209.36</b></FONT> <FONT color="#666666" size="1">CAD</font>
								
								
						
					</div>
					<div style="clear:both;margin-top:2px; text-align:left;">
						
						
						
						
						
						
								
									
									
								
						
						
						
						
						
							
							
							
								<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews"> (<A title="SKU: 66354&#10;Mfr part #: CMZ16GX3M2A1600C10" href="https://www.ncix.com/detail/corsair-vengeance-black-cmz16gx3m2a1600c10-16gb-d3-66354.htm">50</A>)
							
						

					</div>
				</div>
			</td>
		
		
	
		
		
		
		
		
		
		
			
			
		
		
		
		

		

		
			
			
		

		

		
			<td width="33%" valign="top"  style="border-bottom:1px #e8e8e8 solid;border-right:1px #e8e8e8 solid;">
				<div style="padding:10px">
					<div>
							<div style="float:left; width:70%;text-align:center">
								<A class="normal" href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/images/73133_l.jpg" border="0" style="width:80%;height:auto; max-width:100%"  alt="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red" title="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red"></a>
							</div>
							<div style="float:right;width:30%;padding-top:20px;">
								
								
									<A href="https://www.ncix.com/vendor/g-skill-5f-3502.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/3502-s.gif" border="0" width="80" height="40" alt="G.Skill" title="G.Skill"></a>
								
							</div>
					</div>
					<div style="clear:both; text-align:left; padding-top:12px;">
						<A title="SKU: 73133&#10;Mfr part #: F3%2D12800CL10D%2D16GBXL" href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm" style="font-size:1.2em">G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red</A>

					</div>
					<div style="clear:both;margin-top:5px; text-align:left; ">
						
								
								
								<strong>Price:&nbsp;</strong>
								<FONT color="#cc3300" size="2"><b>$219.98</b></FONT> <FONT color="#666666" size="1">CAD</font>
								
								
						
					</div>
					<div style="clear:both;margin-top:2px; text-align:left;">
						
						
						
						
						
						
								
									
									
								
						
						
						
						
						
							
							
							
								<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews"> (<A title="SKU: 73133&#10;Mfr part #: F3-12800CL10D-16GBXL" href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm">55</A>)
							
						

					</div>
				</div>
			</td>
		
		
	
	
		
		
			<td width="33%" style="border-bottom:1px #e8e8e8 solid;;border-left:1px #e8e8e8 solid;">&nbsp;</td>
		
		</tr>
	
	</table>

<style>
.single {
position: absolute;
height: 16px;
line-height: 16px;
width: 18px;
margin: 3px 0 0 0px;
background: #3297fd;
text-align: center;
color: #ffffff;
font-size: 9pt;
font-weight: bold;
border: 0 #3285A7 solid;
-moz-border-radius: 2px;
-webkit-border-radius: 2px;
-khtml-border-radius: 2px;
border-radius: 2px;
}
</style>


	
	
	
	



	
	
	
	
	
	
	
	
		
<script type="text/javascript">
/* https://www.menucool.com/tabbed-content Free to use. v2013.7.6 */
(function(){var g=function(a){
if(a&&a.stopPropagation)a.stopPropagation();
else window.event.cancelBubble=true;
var b=a?a:window.event;b.preventDefault&&b.preventDefault()},d=function(a,c,b){
if(a.addEventListener)a.addEventListener(c,b,false);else a.attachEvent&&a.attachEvent("on"+c,b)
},a=function(c,a){var b=new RegExp("(^| )"+a+"( |$)");return b.test(c.className)?true:false},j=function(b,c,d){if(!a(b,c))if(b.className=="")b.className=c;else if(d)b.className=c+" "+b.className;else b.className+=" "+c},h=function(a,b){var c=new RegExp("(^| )"+b+"( |$)");a.className=a.className.replace(c,"$1");a.className=a.className.replace(/ $/,"")},e=function(){var b=window.location.pathname;if(b.indexOf("/")!=-1)b=b.split("/");var a=b[b.length-1]||"root";if(a.indexOf(".")!=-1)a=a.substring(0,a.indexOf("."));if(a>20)a=a.substring(a.length-19);return a},c="mi"+e(),b=function(b,a){this.g(b,a)};b.prototype={h:function(){var b=new RegExp(c+this.a+"=(\\d+)"),a=document.cookie.match(b);return a?a[1]:this.i()},i:function(){for(var b=0,c=this.b.length;b<c;b++)if(a(this.b[b].parentNode,"selected"))return b;return 0},j:function(b,d){var c=document.getElementById(b.TargetId);if(!c)return;this.l(c);for(var a=0;a<this.b.length;a++)
if(this.b[a]==b){
j(b.parentNode,"selected");
d&&this.d&&this.k(this.a,a)
}else h(this.b[a].parentNode,"selected")},
k:function(a,b){document.cookie=c+a+"="+b+"; path=/"},
l:function(b){for(var a=0;a<this.c.length;a++)this.c[a].style.display=this.c[a].id==b.id?"block":"none"},
m:function(){this.c=[];
for(var c=this,a=0;a<this.b.length;a++){
var b=document.getElementById(this.b[a].TargetId);if(b){this.c.push(b);d(this.b[a],"click",function(b){var a=this;if(a===window)a=window.event.srcElement;c.j(a,1);g(b);return false})}}},g:function(f,h){this.a=h;this.b=[];for(var e=f.getElementsByTagName("a"),i=/#([^?]+)/,a,b,c=0;c<e.length;c++){b=e[c];a=b.getAttribute("href");if(a.indexOf("#")==-1)continue;else{var d=a.match(i);if(d){a=d[1];b.TargetId=a;this.b.push(b)}else continue}}var g=f.getAttribute("data-persist")||"";this.d=g.toLowerCase()=="true"?1:0;this.m();this.n()},n:function(){var a=this.d?parseInt(this.h()):this.i();if(a>=this.b.length)a=0;this.j(this.b[a],0)}};var k=[],i=function(e){var b=false;function a(){
if(b)return;b=true;setTimeout(e,4)}if(document.addEventListener)document.addEventListener("DOMContentLoaded",a,false);
else if(document.attachEvent){try{var f=window.frameElement!=null}catch(g){}if(document.documentElement.doScroll&&!f){function c(){if(b)return;try{document.documentElement.doScroll("left");a()}catch(d){
setTimeout(c,10)}}c()}document.attachEvent("onreadystatechange",function(){document.readyState==="complete"&&a()})
}d(window,"load",a)},f=function(){for(var d=document.getElementsByTagName("ul"),c=0,e=d.length;c<e;c++)a(d[c],"tabs")&&k.push(new b(d[c],c))};i(f);return{}})()
</script>
<style>
/* Tab Content - menucool.com */
#Tab2 {	display:none;	}
#Tab3 {	display:none;	}
#Tab4 {	display:none;	}
#Tab5 {	display:none;	}
#Tab6 {	display:none;	}
#Tab7 {	display:none;	}
ul.tabs
{
padding-top:7px;
padding-bottom:1px;
padding-left:0px;
padding-right:0px;
font-size: 0;
margin:0;
list-style-type: none;
text-align: left; /*set to left, center, or right to align the tabs as desired*/
}
@-moz-document url-prefix() {
ul.tabs {
padding-bottom:0px;
}
}
ul.tabs li
{
display: inline;
margin: 0;
margin-right:3px; /*distance between tabs*/
}
ul.tabs li a
{
font: normal 12px Verdana;
text-decoration: none;
position: relative;
padding: 7px 16px;
border: 1px solid #CCC;
border-bottom:0px;
border-bottom-color:#B7B7B7;
color: #000;
background: #f5f8f9 0 0 repeat-x;
border-radius: 3px 3px 0 0;
outline:none;
}
ul.tabs li a:visited
{
color: #000;
}
ul.tabs li a:hover
{
border: 1px solid #B7B7B7;
border-bottom:0px;
background:#e1f2f9 0 -36px repeat-x;
}
ul.tabs li.selected a, ul.tabs li.selected a:hover
{
position: relative;
top: 0px;
font-weight:bold;
background: white;
border: 1px solid #B7B7B7;
border-bottom-color: white;
}
ul.tabs li.selected a:hover
{
text-decoration: none;
}
div.tabcontents
{
border: 1px solid #B7B7B7; padding: 30px;
background-color:#FFF;
border-radius: 0 3px 3px 3px;
}
.fccontentwrap {
width:950px;
overflow: auto;
margin-left:auto;
margin-right:auto;
margin-bottom:0px;
}
.view-content-text {
font-family: Arial, Helvetica, sans-serif;
font-size: 16px;
font-weight: 300;
line-height: 18px; color: #222222;
text-decoration:none;
margin-top:2px;
padding-top:0px;
padding-bottom:0px;
margin-bottom:0px;
}
.h3-title {
font-family: Arial, Helvetica, sans-serif;
font-size: 26px;
line-height: 16px;
color: #222222;
text-decoration:none;
text-transform:uppercase;
margin-top:8px;
margin-bottom:8px;
padding-bottom:12px;
}

.button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 16px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    -webkit-transition-duration: 0.3s; /* Safari */
    transition-duration: 0.3s;
    cursor: pointer;
	
	    border: 2px solid #008CBA;
}

 

.button2:hover {
    background-color: white; 
    color: black; 
    border: 2px solid #008CBA;
}

.button2 {
    background-color: #008CBA;
    color: white;
}

.button3:hover {
    background-color: white; 
    color: black; 
    border: 2px solid #f44336;
}

.button3 {
    background-color: #f44336;
    color: white;
}

 

</style>
<!-- <link href="template1/tabcontent.css" rel="stylesheet" type="text/css" />-->
<br>
<div class="fccontentwrap">
<div style="width: 90%; margin: 0 auto; padding: 30px 0 25px;">
<ul class="tabs" data-persist="false">
<li class="selected">
<a href="#Tab1">Overview</a></li>
<li><a href="#Tab2">What is RAM?</a></li>
<li><a href="#Tab3">Find the right DDR3 for your system</a></li>
</ul>
<div class="tabcontents">
<div id="Tab1">
<h3 class="h3-title">
DDR3 Memory
</h3>
<p class="view-content-text">
If only we could download more RAM for our computers, then we wouldn't have to go buy some at NCIX every time we want to upgrade our systems. Unfortunately, incorporating volatile Random Access Memory into your PC isn't that easy. Although, it isn't that hard either. DDR3 memory (DDR3 DIMM) is the most common RAM memory on the market. Increasing your system's RAM can result in better performance and an improved multitasking experience, allowing you to run more memory intensive applications without a decrease in speed. What we're trying to say is come visit NCIX and buy RAM.</p>
<br>
<p class="view-content-text">Maximize the performance of your gaming PC, desktop, server, and workstation with our wide selection of DDR3 RAM (DDR3 DIMM) from top vendors such as <a href="https://www.ncix.com/category/ddr3-desktop-memory-17-1303.htm#Kingston">Kingston</a>, <a href="https://www.ncix.com/category/ddr3-desktop-memory-17-1303.htm#Corsair">Corsair</a>, <a href="https://www.ncix.com/category/ddr3-desktop-memory-17-1303.htm#CRUCIAL%20TECHNOLOGY">Crucial </a>and <a href="https://www.ncix.com/category/ddr3-desktop-memory-17-1303.htm#AData%20Technology">ADATA</a></p>
<!--<br><br><center><iframe width="560" height="315" src="https://www.youtube.com/embed/IR0e9hdSkI0" frameborder="0" allowfullscreen></iframe></center>-->
</p>
</div>
<div id="Tab2">
<h3 class="h3-title">NCIX sells sheep?</h3>
<p class="view-content-text">
No, we don't sell horned livestock at NCIX. And you can't put one into your computers either, so don't try it. The type of RAM we have here stands for Random Access Memory. For those who don't know what RAM is, allow NCIX to enlighten you. Think of it as serving plates. The user runs an application and the system requested the data — that's the food cooking in the kitchen. After a couple milli-seconds (6-star chef), that data is then transferred to the serving plates and is easily accessible for anyone (or any program) that needs it. The more RAM you have, the bigger your plate; the larger the plate, the more food/data can be stored. But be warned, more is not always better with RAM. If you had 100GB of RAM, chances are you won't be able to use it all. In that case, you'll just be wasting money, power, and probably space in your system.
</p>
</div>

<div id="Tab3">
<h3 class="h3-title">Memory Configurator</h3>
<p class="view-content-text">
Not sure what memory to get? Use one of these handy memory configurators to find out the right RAM for your system!</p>
<br>
<p class="view-content-text">

<a class="button button2" href="/kingston.php">Kingston Memory Configurator</a>
<!--
<a class="button button3" href="https://www.ncix.com/article/Corsair_Configurators.htm">Corsair Memory Configurator</a>
 -->

 
</p>
</div>

</div>
</div>
</div>
	


<br>

<table width="98%" border="0" cellpadding="8" cellspacing="0" class="normal" align="left">
		 <tr>
		 	<td colspan="5" class="listing">
				<table width="100%" cellpadding="0" cellspacing="0" class="normal">
					<tr valign="top" align="left">
						
						
						
						
						<td><h3 style="font-weight:normal; font-size:14px;">Top <strong>10</strong> most popular <font color="#CC0000"><strong>DDR3 Memory</strong></font></h3></td>
						
						
					</tr>

				 </table>
			</td>
		 </tr>
		 <tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
		 
			<td	class="linehead">&nbsp;</td>
			<td	class="linehead"><font color="#666666" style="font-size:10pt"><strong>Description</strong></font></td>
			<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
			<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
			
		  </tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
				
				
					
					
					
					
					
				
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/kingston-16gb-240-pin-ddr3-sdram-a1-96950.htm?promoid=1374"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/96950.jpg" border="0" width="300" height="150" title="Kingston 16GB 240-PIN DDR3 SDRAM DDR3 1866 (PC3 14900) ECC Registered Server Memory" alt="Kingston 16GB 240-PIN DDR3 SDRAM DDR3 1866 (PC3 14900) ECC Registered Server Memory"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/kingston-e5-98.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/98-s.gif" border="0" title="Kingston" alt="Kingston"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">1</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/kingston-16gb-240-pin-ddr3-sdram-a1-96950.htm?promoid=1374" style="font-size:10pt">Kingston 16GB 240-PIN DDR3 SDRAM DDR3 1866 (PC3 14900) ECC Registered Server Memory</a> <font size="1">(KVR18R13D4/16)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					
					
					
					
					
						
						
					
					
					
						<font color="#CC0000">Save $70.99</font> off our regular price of $270.98<br>
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('96950')" title="NCIX.com Real Time Stock Check"><font color="#669900">In&nbsp;Stock</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#cc0000" class="listing"><strong>$199.99</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
				
				
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95971.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/95971.jpg" border="0" width="300" height="150" title="Kingston HyperX Fury Memory Black 16GB 2x8GB DDR3-1866 CL10 Dual Channel Memory Kit" alt="Kingston HyperX Fury Memory Black 16GB 2x8GB DDR3-1866 CL10 Dual Channel Memory Kit"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/kingston-e5-98.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/98-s.gif" border="0" title="Kingston" alt="Kingston"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">2</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95971.htm" style="font-size:10pt">Kingston HyperX Fury Memory Black 16GB 2x8GB DDR3-1866 CL10 Dual Channel Memory Kit</a> <font size="1">(HX318C10FBK2/16)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95971.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 107 Customer Reviews</font></a><br>
						
					
					
					
					
					
						
						
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('95971')" title="NCIX.com Real Time Stock Check"><font color="#669900">In&nbsp;Stock</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$167.19</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/corsair-vengeance-cmz12gx3m3a1600c9-12gb-3x4gb-2e-57080.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/57080.jpg" border="0" width="300" height="150" title="Corsair Vengeance CMZ12GX3M3A1600C9 12GB 3X4GB DDR3-1600 CL9 Triple Channel Memory Kit" alt="Corsair Vengeance CMZ12GX3M3A1600C9 12GB 3X4GB DDR3-1600 CL9 Triple Channel Memory Kit"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/corsair-9e-135.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/135-s.gif" border="0" title="Corsair" alt="Corsair"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">3</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/corsair-vengeance-cmz12gx3m3a1600c9-12gb-3x4gb-2e-57080.htm" style="font-size:10pt">Corsair Vengeance CMZ12GX3M3A1600C9 12GB 3X4GB DDR3-1600 CL9 Triple Channel Memory Kit</a> <font size="1">(CMZ12GX3M3A1600C9)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/corsair-vengeance-cmz12gx3m3a1600c9-12gb-3x4gb-2e-57080.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 37 Customer Reviews</font></a><br>
						
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('57080')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$169.98</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/kingston-kvr1333d3n9-8g-8gb-1333mhz-ddr3-a9-65772.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/65772.jpg" border="0" width="300" height="150" title="Kingston KVR1333D3N9/8G 8GB 1333MHz DDR3 NON-ECC CL9 DIMM" alt="Kingston KVR1333D3N9/8G 8GB 1333MHz DDR3 NON-ECC CL9 DIMM"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/kingston-e5-98.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/98-s.gif" border="0" title="Kingston" alt="Kingston"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">4</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/kingston-kvr1333d3n9-8g-8gb-1333mhz-ddr3-a9-65772.htm" style="font-size:10pt">Kingston KVR1333D3N9/8G 8GB 1333MHz DDR3 NON-ECC CL9 DIMM</a> <font size="1">(KVR1333D3N9/8G)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.gif"   align="top"  alt="4 of 5 customer reviews" title="4 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/kingston-kvr1333d3n9-8g-8gb-1333mhz-ddr3-a9-65772.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 2 Customer Reviews</font></a><br>
						
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('65772')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$84.99</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/kingston-kvr13n9s8k2-8-8gb-2x4gb-kits-6a-88587.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/88587.jpg" border="0" width="300" height="150" title="Kingston KVR13N9S8K2/8 8GB 2x4GB Kits DDR3-1333MHZ DIMM Non-ECC Sr X8 CL9 Gold Single Rank Memory" alt="Kingston KVR13N9S8K2/8 8GB 2x4GB Kits DDR3-1333MHZ DIMM Non-ECC Sr X8 CL9 Gold Single Rank Memory"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/kingston-e5-98.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/98-s.gif" border="0" title="Kingston" alt="Kingston"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">5</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/kingston-kvr13n9s8k2-8-8gb-2x4gb-kits-6a-88587.htm" style="font-size:10pt">Kingston KVR13N9S8K2/8 8GB 2x4GB Kits DDR3-1333MHZ DIMM Non-ECC Sr X8 CL9 Gold Single Rank Memory</a> <font size="1">(KVR13N9S8K2/8)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('88587')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$86.51</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/kingston-kvr16n11s8-4-4gb-ddr3-1600mhz-c7-88613.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/88613.jpg" border="0" width="300" height="150" title="Kingston KVR16N11S8/4 4GB DDR3 1600MHz 240PIN DIMM Unbuff CL11 1.5V Gold Memory" alt="Kingston KVR16N11S8/4 4GB DDR3 1600MHz 240PIN DIMM Unbuff CL11 1.5V Gold Memory"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/kingston-e5-98.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/98-s.gif" border="0" title="Kingston" alt="Kingston"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">6</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/kingston-kvr16n11s8-4-4gb-ddr3-1600mhz-c7-88613.htm" style="font-size:10pt">Kingston KVR16N11S8/4 4GB DDR3 1600MHz 240PIN DIMM Unbuff CL11 1.5V Gold Memory</a> <font size="1">(KVR16N11S8/4)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/kingston-kvr16n11s8-4-4gb-ddr3-1600mhz-c7-88613.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 4 Customer Reviews</font></a><br>
						
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('88613')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$52.04</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
				
				
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/73133.jpg" border="0" width="300" height="150" title="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red" alt="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/g-skill-5f-3502.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/3502-s.gif" border="0" title="G.Skill" alt="G.Skill"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">7</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm" style="font-size:10pt">G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red</a> <font size="1">(F3-12800CL10D-16GBXL)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 55 Customer Reviews</font></a><br>
						
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('73133')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$219.98</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
				
				
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-8gb-2x4gb-01-57953.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/57953.jpg" border="0" width="300" height="150" title="G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1600 CL9-9-9-24 1.5V 240PIN Dual Channel Memory Kit - Red" alt="G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1600 CL9-9-9-24 1.5V 240PIN Dual Channel Memory Kit - Red"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/g-skill-5f-3502.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/3502-s.gif" border="0" title="G.Skill" alt="G.Skill"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">8</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/g-skill-ripjaws-x-8gb-2x4gb-01-57953.htm" style="font-size:10pt">G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1600 CL9-9-9-24 1.5V 240PIN Dual Channel Memory Kit - Red</a> <font size="1">(F3-12800CL9D-8GBXL)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-8gb-2x4gb-01-57953.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 274 Customer Reviews</font></a><br>
						
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('57953')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$119.99</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
				
				
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95956.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/95956.jpg" border="0" width="300" height="150" title="Kingston HyperX Fury Memory Black 8GB 2X4GB DDR3-1600 CL10 Dual Channel Memory Kit" alt="Kingston HyperX Fury Memory Black 8GB 2X4GB DDR3-1600 CL10 Dual Channel Memory Kit"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/kingston-e5-98.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/98-s.gif" border="0" title="Kingston" alt="Kingston"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">9</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95956.htm" style="font-size:10pt">Kingston HyperX Fury Memory Black 8GB 2X4GB DDR3-1600 CL10 Dual Channel Memory Kit</a> <font size="1">(HX316C10FBK2/8)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95956.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 48 Customer Reviews</font></a><br>
						
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('95956')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$102.50</strong>
						
						

					
				</td>
				
			</tr>
		  
		  	
			
			
			
			
			
				
				
			
			
			
			
			
			
			

			<tr align="left" valign="top">
				
				<td class="line" align="center" width="300">
					<div>
					
					
					<a href="https://www.ncix.com/detail/corsair-vengeance-black-cmz16gx3m2a1600c10-16gb-d3-66354.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/gif/66354.jpg" border="0" width="300" height="150" title="Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit" alt="Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit"></a>
					</div>
					<div style="margin-top:6px">
					

					
						<A class="normal" href="https://www.ncix.com/vendor/corsair-9e-135.htm"><img src="https://d1sfu4378rr01a.cloudfront.net/v/135-s.gif" border="0" title="Corsair" alt="Corsair"></a>
					
					</div>

				</td>
				<td class="line" align="left">
					<div>
						<div style="float:left">
							<span class="single">10</span>
						</div>
						<div style="float:left;margin-left:25px">
						  <span class="listing"><a href="https://www.ncix.com/detail/corsair-vengeance-black-cmz16gx3m2a1600c10-16gb-d3-66354.htm" style="font-size:10pt">Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit</a> <font size="1">(CMZ16GX3M2A1600C10)</font></span>
						</div>
					</div>
					<div style="margin-top:12px;text-align:left; float:left; clear:both">
					

					
					
					
					
					
					
					

						
						
						
							<img src="https://source.ncix.com/Review-stars/images1/img_stars_4.5.gif"   align="top"  alt="4.5 of 5 customer reviews" title="4.5 of 5 customer reviews">
							<a href="https://www.ncix.com/detail/corsair-vengeance-black-cmz16gx3m2a1600c10-16gb-d3-66354.htm#CustomerReviews" target="_blank"><font color="#3300FF" size="1"> 50 Customer Reviews</font></a><br>
						
					
					
					
					
						
							Back Order
						
						
					
					
					
					
					</div>
				</td>
				<td class="line" align="center" nowrap="nowrap">
						<b><a href="javascript:checkinventory('66354')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					

						<font color="#333333" class="listing"><strong>$209.36</strong>
						
						

					
				</td>
				
			</tr>
		  
</table>
<br />
<table width="98%" cellpadding="0" cellspacing="0" class="normal" style="padding:10px">
	<tr>
		
		<td align="right">
			<input type="checkbox" id="stockonly" name="stockonly" onclick="productlistfilter()" value="0"    />View in stock only
			<select name="sortby" id="sortby" class="normal" onchange="productlistfilter()">
				<option value="">Sort By</option>
				<option value="1"  >Brand</option>
				<option value="2" >Price</option>
			</select>
		</td>
		
	</tr>
 </table>
 <div id="productlistdiv">
<!--cstart-->


		
		
		
		
		<a name="mtop"></a>
		<table width="98%" cellpadding="0" cellspacing="0"  class="note" align="left">
			<tr>
				<td class="normal" align="left">
					
					
					<a href="#Dell Computer">
					
					Dell Computer(1)
					
					</a>
					
					| 
					<a href="#Corsair">
					
					Corsair(18)
					
					</a>
					
					| 
					<a href="#AData Technology">
					
					AData Technology(1)
					
					</a>
					
					| 
					<a href="#Kingston Branded">
					
					Kingston Branded(6)
					
					</a>
					
					| 
					<a href="#CRUCIAL TECHNOLOGY">
					
					CRUCIAL TECHNOLOGY(4)
					
					</a>
					
					| 
					<a href="#HP SMB Systems">
					
					HP SMB Systems(8)
					
					</a>
					
					| 
					<a href="#Axiom">
					
					Axiom(2)
					
					</a>
					
					| 
					<a href="#Addon">
					
					Addon(15)
					
					</a>
					
					| 
					<a href="#Micron">
					
					Micron(1)
					
					</a>
					
					| 
					<a href="#VISIONTEK">
					
					VISIONTEK(1)
					
					</a>
					
					| 
					<a href="#SuperMicro">
					
					SuperMicro(2)
					
					</a>
					
					| 
					<a href="#Kingston">
					
					Kingston(55)
					
					</a>
					
					| 
					<a href="#GeIL USA - EOL">
					
					GeIL USA - EOL(6)
					
					</a>
					
					| 
					<a href="#Add-On Computer">
					
					Add-On Computer(1)
					
					</a>
					
					| 
					<a href="#QNAP Inc.">
					
					QNAP Inc.(1)
					
					</a>
					
					| 
					<a href="#Cisco">
					
					Cisco(2)
					
					</a>
					
					| 
					<a href="#G.Skill">
					
					G.Skill(4)
					
					</a>
					
					| 
					<a href="#Lenovo">
					
					Lenovo(2)
					
					</a>
					
				</td>
			</tr>
		</table>
		<table width="98%" cellpadding="3" cellspacing="0" class="normal" align="left">
		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="AData Technology"></a>AData Technology - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/54241s.jpg" border="0" width="150" height="75" title="ADATA Gaming Series 4GB 2X2GB DDR3-1333 CL8-8-8-24 Dual Channel Memory Kit W/ Heatsink" alt="ADATA Gaming Series 4GB 2X2GB DDR3-1333 CL8-8-8-24 Dual Channel Memory Kit W/ Heatsink">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/adata-gaming-series-4gb-2x2gb-8a-54241.htm">ADATA Gaming Series 4GB 2X2GB DDR3-1333 CL8-8-8-24 Dual Channel Memory Kit W/ Heatsink</a>
						<font size=1>(AX3U1333GB2G8-2G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('54241')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$140.98</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Add-On Computer"></a>Add-On Computer - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/109343s.jpg" border="0" width="150" height="75" title="2GB DDR3-1066MHZ PC3-8500 240P Industry Standard DIMM F/DESKTOPS" alt="2GB DDR3-1066MHZ PC3-8500 240P Industry Standard DIMM F/DESKTOPS">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/2gb-ddr3-1066mhz-pc3-8500-240p-industry-ee-109343.htm">2GB DDR3-1066MHZ PC3-8500 240P Industry Standard DIMM F/DESKTOPS</a>
						<font size=1>(AA1066D3N7/2G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('109343')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$31.42</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Addon"></a>Addon - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1030036836.jpg" border="0" width="150" height="75" title="Addon 2GB DDR3-1333MHZ Dr Udimm" alt="Addon 2GB DDR3-1333MHZ Dr Udimm">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ddr3-1333mhz-dr-udimm-b7-114228.htm">Addon 2GB DDR3-1333MHZ Dr Udimm</a>
						<font size=1>(576110-001-AAK)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114228')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$32.24</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1028847748.jpg" border="0" width="150" height="75" title="Addon 2GB DDR3-1333MHZ 240PIN F/DELL" alt="Addon 2GB DDR3-1333MHZ 240PIN F/DELL">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ddr3-1333mhz-240pin-f-dell-3e-114225.htm">Addon 2GB DDR3-1333MHZ 240PIN F/DELL</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114225')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$32.24</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/132998s.jpg" border="0" width="150" height="75" title="Addon 16GB DDR3-1333MHZ F/ Lenovo SDRAM" alt="Addon 16GB DDR3-1333MHZ F/ Lenovo SDRAM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-16gb-ddr3-1333mhz-f-lenovo-ac-132998.htm">Addon 16GB DDR3-1333MHZ F/ Lenovo SDRAM</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('132998')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$158.92</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1028847750.jpg" border="0" width="150" height="75" title="Addon 2GB DDR3-1333MHZ 240PIN Lenovo" alt="Addon 2GB DDR3-1333MHZ 240PIN Lenovo">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ddr3-1333mhz-240pin-lenovo-9a-114227.htm">Addon 2GB DDR3-1333MHZ 240PIN Lenovo</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114227')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$32.24</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/114247s.jpg" border="0" width="150" height="75" title="Addon 2GB DDR3-1066MHZ 204-PIN SODIMM" alt="Addon 2GB DDR3-1066MHZ 204-PIN SODIMM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ddr3-1066mhz-204-pin-sodimm-0e-114247.htm">Addon 2GB DDR3-1066MHZ 204-PIN SODIMM</a>
						<font size=1>(PA3856U-1M2G-AAK)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114247')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$34.15</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/114234s.jpg" border="0" width="150" height="75" title="Addon 2GB DDR3-1333MHZ PC3-10600 240P" alt="Addon 2GB DDR3-1333MHZ PC3-10600 240P">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ddr3-1333mhz-pc3-10600-240p-03-114234.htm">Addon 2GB DDR3-1333MHZ PC3-10600 240P</a>
						<font size=1>(AA1333D3N9/2G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114234')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$32.24</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1028847723.jpg" border="0" width="150" height="75" title="Addon 2GB DDR3-1333MHZ 240PIN F/HP" alt="Addon 2GB DDR3-1333MHZ 240PIN F/HP">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ddr3-1333mhz-240pin-f-hp-8b-114223.htm">Addon 2GB DDR3-1333MHZ 240PIN F/HP</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114223')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$32.24</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1028879329.jpg" border="0" width="150" height="75" title="Addon 500670-B21-AMK 2GB 1333MHz DDR3 ECC Dr X8 F/HP" alt="Addon 500670-B21-AMK 2GB 1333MHz DDR3 ECC Dr X8 F/HP">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-500670-b21-amk-2gb-1333mhz-ddr3-fa-114370.htm">Addon 500670-B21-AMK 2GB 1333MHz DDR3 ECC Dr X8 F/HP</a>
						<font size=1>(500670-B21-AMK)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114370')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$43.61</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/114374s.jpg" border="0" width="150" height="75" title="Addon 2GB ECC DDR3 1333MHz 240-PIN" alt="Addon 2GB ECC DDR3 1333MHz 240-PIN">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ecc-ddr3-1333mhz-7e-114374.htm">Addon 2GB ECC DDR3 1333MHz 240-PIN</a>
						<font size=1>(AM1333D3DRE/2G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114374')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$43.61</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1028879267.jpg" border="0" width="150" height="75" title="Addon 2GB ECC DDR3-1333MHZ F/LENOVO" alt="Addon 2GB ECC DDR3-1333MHZ F/LENOVO">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/addon-2gb-ecc-ddr3-1333mhz-f-lenovo-e7-114368.htm">Addon 2GB ECC DDR3-1333MHZ F/LENOVO</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114368')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$43.61</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
			
				<tr>
					<td></td>
					
					<td colspan="3"><img src="/_img/btn_arrow.gif"  border="0"/> <a href="https://www.ncix.com/list/ddr3-memory-addon-d0-1303-4950.htm" style="color:#000000">More <strong>Addon</strong> DDR3 Memory</a></td>
				</tr>
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Axiom"></a>Axiom - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/112858s.jpg" border="0" width="150" height="75" title="Axiom Memory 2GB DDR3-1066 Udimm for Lenovo # 45J5435" alt="Axiom Memory 2GB DDR3-1066 Udimm for Lenovo # 45J5435">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/axiom-memory-2gb-ddr3-1066-udimm-a5-112858.htm">Axiom Memory 2GB DDR3-1066 Udimm for Lenovo # 45J5435</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('112858')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$31.68</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/112822s.jpg" border="0" width="150" height="75" title="Axiom Memory 2GB DDR3-1600 Udimm F/0A65728" alt="Axiom Memory 2GB DDR3-1600 Udimm F/0A65728">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/axiom-memory-2gb-ddr3-1600-udimm-b9-112822.htm">Axiom Memory 2GB DDR3-1600 Udimm F/0A65728</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('112822')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$31.68</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Cisco"></a>Cisco - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/images/space.gif" border="0" width="150" height="75" title="CISCO 16GB DUAL RANK DDR3-1600MHZ DIMM" alt="CISCO 16GB DUAL RANK DDR3-1600MHZ DIMM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/cisco-16gb-dual-rank-ddr3-1600mhz-7f-133113.htm">CISCO 16GB DUAL RANK DDR3-1600MHZ DIMM</a>
						<font size=1>(UCS-MR-1X162RY-A=)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('133113')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$528.82</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/images/space.gif" border="0" width="150" height="75" title="CISCO 8GB DDR3/1866-MHZ RDIMM" alt="CISCO 8GB DDR3/1866-MHZ RDIMM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/cisco-8gb-ddr3-1866-mhz-rdimm-13-114699.htm">CISCO 8GB DDR3/1866-MHZ RDIMM</a>
						<font size=1>(UCS-MR-1X082RZ-A=)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114699')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$304.36</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Corsair"></a>Corsair - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/66354s.jpg" border="0" width="150" height="75" title="Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit" alt="Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-vengeance-black-cmz16gx3m2a1600c10-16gb-d3-66354.htm">Corsair Vengeance Black CMZ16GX3M2A1600C10 16GB 2x8GB DDR3-1600 CL10 1.5V Dual Channel Memory Kit</a>
						<font size=1>(CMZ16GX3M2A1600C10)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('66354')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$209.36</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/57080s.jpg" border="0" width="150" height="75" title="Corsair Vengeance CMZ12GX3M3A1600C9 12GB 3X4GB DDR3-1600 CL9 Triple Channel Memory Kit" alt="Corsair Vengeance CMZ12GX3M3A1600C9 12GB 3X4GB DDR3-1600 CL9 Triple Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-vengeance-cmz12gx3m3a1600c9-12gb-3x4gb-2e-57080.htm">Corsair Vengeance CMZ12GX3M3A1600C9 12GB 3X4GB DDR3-1600 CL9 Triple Channel Memory Kit</a>
						<font size=1>(CMZ12GX3M3A1600C9)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('57080')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$169.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/53427s.jpg" border="0" width="150" height="75" title="Corsair XMS CMX8GX3M2A1333C9 8GB 2X4GB DDR3-1333 CL9-9-9-24 Dual Channel Memory Kit" alt="Corsair XMS CMX8GX3M2A1333C9 8GB 2X4GB DDR3-1333 CL9-9-9-24 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-xms-cmx8gx3m2a1333c9-8gb-2x4gb-94-53427.htm">Corsair XMS CMX8GX3M2A1333C9 8GB 2X4GB DDR3-1333 CL9-9-9-24 Dual Channel Memory Kit</a>
						<font size=1>(CMX8GX3M2A1333C9)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('53427')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$96.46</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/59431s.jpg" border="0" width="150" height="75" title="Corsair Vengeance Blue CMZ8GX3M2A1600C9B 8GB 2x4GB DDR3-1600 CL9-9-9-24 Dual Channel Memory Kit" alt="Corsair Vengeance Blue CMZ8GX3M2A1600C9B 8GB 2x4GB DDR3-1600 CL9-9-9-24 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-vengeance-blue-cmz8gx3m2a1600c9b-8gb-5d-59431.htm">Corsair Vengeance Blue CMZ8GX3M2A1600C9B 8GB 2x4GB DDR3-1600 CL9-9-9-24 Dual Channel Memory Kit</a>
						<font size=1>(CMZ8GX3M2A1600C9B)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('59431')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$113.08</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/57078s.jpg" border="0" width="150" height="75" title="Corsair Vengeance 8GB 2x4GB DDR3 1600MHz CL9-9-9-24 Dual Channel Memory Kit" alt="Corsair Vengeance 8GB 2x4GB DDR3 1600MHz CL9-9-9-24 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-vengeance-8gb-2x4gb-ddr3-e4-57078.htm">Corsair Vengeance 8GB 2x4GB DDR3 1600MHz CL9-9-9-24 Dual Channel Memory Kit</a>
						<font size=1>(CMZ8GX3M2A1600C9)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('57078')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$113.08</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/61961s.jpg" border="0" width="150" height="75" title="Corsair Vengeance CML8GX3M2A1600C9 Lowprofile 8GB 2X4GB DDR3-1600 CL9-9-9-24 Dual Channel Memory Kit" alt="Corsair Vengeance CML8GX3M2A1600C9 Lowprofile 8GB 2X4GB DDR3-1600 CL9-9-9-24 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-vengeance-cml8gx3m2a1600c9-lowprofile-8gb-ce-61961.htm">Corsair Vengeance CML8GX3M2A1600C9 Lowprofile 8GB 2X4GB DDR3-1600 CL9-9-9-24 Dual Channel Memory Kit</a>
						<font size=1>(CML8GX3M2A1600C9)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('61961')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$90.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/55048s.jpg" border="0" width="150" height="75" title="Corsair XMS CMX4GX3M1A1333C9 4GB 1X4GB DDR3-1333 CL9-9-9-24 DIMM Memory Module" alt="Corsair XMS CMX4GX3M1A1333C9 4GB 1X4GB DDR3-1333 CL9-9-9-24 DIMM Memory Module">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-xms-cmx4gx3m1a1333c9-4gb-1x4gb-47-55048.htm">Corsair XMS CMX4GX3M1A1333C9 4GB 1X4GB DDR3-1333 CL9-9-9-24 DIMM Memory Module</a>
						<font size=1>(CMX4GX3M1A1333C9)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('55048')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$54.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/54791s.jpg" border="0" width="150" height="75" title="Corsair 4GB 1X4GB DDR3 1333MHz CL9 Memory Module" alt="Corsair 4GB 1X4GB DDR3 1333MHz CL9 Memory Module">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-4gb-1x4gb-ddr3-1333mhz-62-54791.htm">Corsair 4GB 1X4GB DDR3 1333MHz CL9 Memory Module</a>
						<font size=1>(CMV4GX3M1A1333C9)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('54791')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$53.79</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/72016s.jpg" border="0" width="150" height="75" title="Corsair Vengeance 16GB 2x8GB DDR3 1600MHz CL9 Dual Channel Memory Kit" alt="Corsair Vengeance 16GB 2x8GB DDR3 1600MHz CL9 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-vengeance-16gb-2x8gb-ddr3-27-72016.htm">Corsair Vengeance 16GB 2x8GB DDR3 1600MHz CL9 Dual Channel Memory Kit</a>
						<font size=1>(CMZ16GX3M2A1600C9)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('72016')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$215.00</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/64473s.jpg" border="0" width="150" height="75" title="Corsair Vengeance CMZ8GX3M1A1600C10 8GB 1X8GB DDR3-1600 CL10-10-10-27 240PIN Single Memory Module" alt="Corsair Vengeance CMZ8GX3M1A1600C10 8GB 1X8GB DDR3-1600 CL10-10-10-27 240PIN Single Memory Module">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/corsair-vengeance-cmz8gx3m1a1600c10-8gb-1x8gb-34-64473.htm">Corsair Vengeance CMZ8GX3M1A1600C10 8GB 1X8GB DDR3-1600 CL10-10-10-27 240PIN Single Memory Module</a>
						<font size=1>(CMZ8GX3M1A1600C10)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('64473')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$104.42</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
			
				<tr>
					<td></td>
					
					<td colspan="3"><img src="/_img/btn_arrow.gif"  border="0"/> <a href="https://www.ncix.com/list/ddr3-memory-corsair-46-1303-135.htm" style="color:#000000">More <strong>Corsair</strong> DDR3 Memory</a></td>
				</tr>
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="CRUCIAL TECHNOLOGY"></a>CRUCIAL TECHNOLOGY - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/134796s.jpg" border="0" width="150" height="75" title="Crucial CT102464BD160B 8GB (1x8GB) DDR3L 1600 CL11 1.35V UDIMM Desktop Memory" alt="Crucial CT102464BD160B 8GB (1x8GB) DDR3L 1600 CL11 1.35V UDIMM Desktop Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/crucial-ct102464bd160b-8gb-1x8gb-ddr3l-df-134796.htm">Crucial CT102464BD160B 8GB (1x8GB) DDR3L 1600 CL11 1.35V UDIMM Desktop Memory</a>
						<font size=1>(CT102464BD160B)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('134796')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$104.72</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/68899s.jpg" border="0" width="150" height="75" title="Crucial Ballistix Sport 16GB 2X8GB PC3-12800 DDR3-1600 1.5V CL9 Dual Channel Memory Kit" alt="Crucial Ballistix Sport 16GB 2X8GB PC3-12800 DDR3-1600 1.5V CL9 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/crucial-ballistix-sport-16gb-2x8gb-ca-68899.htm">Crucial Ballistix Sport 16GB 2X8GB PC3-12800 DDR3-1600 1.5V CL9 Dual Channel Memory Kit</a>
						<font size=1>(BLS2KIT8G3D1609DS1S00)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
								
								
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('68899')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$206.80</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/106469s.jpg" border="0" width="150" height="75" title="Crucial Memory CT2KIT102472BD160B 16GB(2X8) Kit DDR3 PC3 12800 ECC UDIMM 240P" alt="Crucial Memory CT2KIT102472BD160B 16GB(2X8) Kit DDR3 PC3 12800 ECC UDIMM 240P">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/crucial-memory-ct2kit102472bd160b-16gb-2x8-kit-c9-106469.htm">Crucial Memory CT2KIT102472BD160B 16GB(2X8) Kit DDR3 PC3 12800 ECC UDIMM 240P</a>
						<font size=1>(CT2KIT102472BD160B)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('106469')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$261.30</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/119064s.jpg" border="0" width="150" height="75" title="Crucial Memory CT16G3ERSDD4186D 16GB DDR3 1866 ECC Registered 1.5V Retail" alt="Crucial Memory CT16G3ERSDD4186D 16GB DDR3 1866 ECC Registered 1.5V Retail">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/crucial-memory-ct16g3ersdd4186d-16gb-ddr3-cb-119064.htm">Crucial Memory CT16G3ERSDD4186D 16GB DDR3 1866 ECC Registered 1.5V Retail</a>
						<font size=1>(CT16G3ERSDD4186D)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('119064')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$263.18</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Dell Computer"></a>Dell Computer - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1023541239.jpg" border="0" width="150" height="75" title="DELL 8GB 1600MHZ DELL CERTIFIED DDR3 SDRAM" alt="DELL 8GB 1600MHZ DELL CERTIFIED DDR3 SDRAM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/dell-8gb-1600mhz-dell-certified-e2-132970.htm">DELL 8GB 1600MHZ DELL CERTIFIED DDR3 SDRAM</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('132970')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$162.82</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="G.Skill"></a>G.Skill - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/57953s.jpg" border="0" width="150" height="75" title="G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1600 CL9-9-9-24 1.5V 240PIN Dual Channel Memory Kit - Red" alt="G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1600 CL9-9-9-24 1.5V 240PIN Dual Channel Memory Kit - Red">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-8gb-2x4gb-01-57953.htm">G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1600 CL9-9-9-24 1.5V 240PIN Dual Channel Memory Kit - Red</a>
						<font size=1>(F3-12800CL9D-8GBXL)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('57953')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$119.99</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/73133s.jpg" border="0" width="150" height="75" title="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red" alt="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm">G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red</a>
						<font size=1>(F3-12800CL10D-16GBXL)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('73133')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$219.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/104837s.jpg" border="0" width="150" height="75" title="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-2133 CL11-13-13-31 1.5V 240PIN Dual Channel Memory Kit - Red" alt="G.SKILL Ripjaws X 16GB (2x8GB) DDR3-2133 CL11-13-13-31 1.5V 240PIN Dual Channel Memory Kit - Red">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-104837.htm">G.SKILL Ripjaws X 16GB (2x8GB) DDR3-2133 CL11-13-13-31 1.5V 240PIN Dual Channel Memory Kit - Red</a>
						<font size=1>(F3-2133C11D-16GXL)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('104837')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$229.99</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/88897s.jpg" border="0" width="150" height="75" title="G.SKILL Ripjaws X 16GB (2X8GB) DDR3-1866 CL10-11-10-30 1.5V 240PIN Dual Channel Memory Kit - Red" alt="G.SKILL Ripjaws X 16GB (2X8GB) DDR3-1866 CL10-11-10-30 1.5V 240PIN Dual Channel Memory Kit - Red">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-88897.htm">G.SKILL Ripjaws X 16GB (2X8GB) DDR3-1866 CL10-11-10-30 1.5V 240PIN Dual Channel Memory Kit - Red</a>
						<font size=1>(F3-14900CL10D-16GBXL)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('88897')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$219.99</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="GeIL USA - EOL"></a>GeIL USA - EOL - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/105407s.jpg" border="0" width="150" height="75" title="Geil Evo Potenza 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - White" alt="Geil Evo Potenza 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - White">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/geil-evo-potenza-16gb-2x8gb-5f-105407.htm">Geil Evo Potenza 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - White</a>
						<font size=1>(GPW316GB1600C11DC)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('105407')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$156.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/105406s.jpg" border="0" width="150" height="75" title="GeIL EVO Potenza 8GB 2X4GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - White" alt="GeIL EVO Potenza 8GB 2X4GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - White">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/geil-evo-potenza-8gb-2x4gb-58-105406.htm">GeIL EVO Potenza 8GB 2X4GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - White</a>
						<font size=1>(GPW38GB1600C11DC)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('105406')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$83.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/105398s.jpg" border="0" width="150" height="75" title="GeIL EVO Potenza 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - Onyx Black" alt="GeIL EVO Potenza 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - Onyx Black">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/geil-evo-potenza-16gb-2x8gb-5f-105398.htm">GeIL EVO Potenza 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - Onyx Black</a>
						<font size=1>(GPB316GB1600C11DC)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('105398')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$150.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/105401s.jpg" border="0" width="150" height="75" title="GeIL Enhance Veloce 8GB 2X4GB DDR3-1600 9-9-9-28 PC3-12800 1.5V Memory Kit - Gold" alt="GeIL Enhance Veloce 8GB 2X4GB DDR3-1600 9-9-9-28 PC3-12800 1.5V Memory Kit - Gold">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/geil-enhance-veloce-8gb-2x4gb-c2-105401.htm">GeIL Enhance Veloce 8GB 2X4GB DDR3-1600 9-9-9-28 PC3-12800 1.5V Memory Kit - Gold</a>
						<font size=1>(GENV38GB1600C9DC)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('105401')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$79.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/105403s.jpg" border="0" width="150" height="75" title="GeIL Black Dragon 8GB 2X4GB 8 Layer PCB w/ Red LED DDR3-1600 9-9-9-28 PC3-12800 1.6V Memory Kit" alt="GeIL Black Dragon 8GB 2X4GB 8 Layer PCB w/ Red LED DDR3-1600 9-9-9-28 PC3-12800 1.6V Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/geil-black-dragon-8gb-2x4gb-20-105403.htm">GeIL Black Dragon 8GB 2X4GB 8 Layer PCB w/ Red LED DDR3-1600 9-9-9-28 PC3-12800 1.6V Memory Kit</a>
						<font size=1>(GB38GB1600C9DC)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('105403')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$79.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/105400s.jpg" border="0" width="150" height="75" title="Geil Evo Veloce 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - Red" alt="Geil Evo Veloce 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - Red">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/geil-evo-veloce-16gb-2x8gb-9f-105400.htm">Geil Evo Veloce 16GB 2X8GB DDR3-1600 11-11-11-28 PC3-12800 1.5V Memory Kit - Red</a>
						<font size=1>(GEV316GB1600C11DC)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('105400')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$152.98</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="HP SMB Systems"></a>HP SMB Systems - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/128520s.jpg" border="0" width="150" height="75" title="HP 4GB DDR3L-1600 DIMM Desktop Memory" alt="HP 4GB DDR3L-1600 DIMM Desktop Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-4gb-ddr3l-1600-dimm-desktop-d7-128520.htm">HP 4GB DDR3L-1600 DIMM Desktop Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('128520')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$80.48</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/113701s.jpg" border="0" width="150" height="75" title="HP 8GB DDR3-1600 DIMM Memory for EliteDesk" alt="HP 8GB DDR3-1600 DIMM Memory for EliteDesk">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-8gb-ddr3-1600-dimm-memory-c3-113701.htm">HP 8GB DDR3-1600 DIMM Memory for EliteDesk</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('113701')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$158.70</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/114717s.jpg" border="0" width="150" height="75" title="HP 16GB 2RX4 DDR3 PC3L-10600R-9" alt="HP 16GB 2RX4 DDR3 PC3L-10600R-9">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-16gb-2rx4-ddr3-pc3l-10600r-9-7d-114717.htm">HP 16GB 2RX4 DDR3 PC3L-10600R-9</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114717')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$590.33</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/128534s.jpg" border="0" width="150" height="75" title="HP 8GB DDR3L-1600 DIMM Desktop Memory" alt="HP 8GB DDR3L-1600 DIMM Desktop Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-8gb-ddr3l-1600-dimm-desktop-47-128534.htm">HP 8GB DDR3L-1600 DIMM Desktop Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('128534')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$129.66</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/104974s.jpg" border="0" width="150" height="75" title="HP 4GB DDR3L-1600 1.35V SODIMM Notebook Memory" alt="HP 4GB DDR3L-1600 1.35V SODIMM Notebook Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-4gb-ddr3l-1600-1-35v-sodimm-4a-104974.htm">HP 4GB DDR3L-1600 1.35V SODIMM Notebook Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('104974')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$73.97</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/87846s.jpg" border="0" width="150" height="75" title="HP 2GB DDR3-1600 PC3-12800 DIMM Desktop Memory" alt="HP 2GB DDR3-1600 PC3-12800 DIMM Desktop Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-2gb-ddr3-1600-pc3-12800-dimm-2a-87846.htm">HP 2GB DDR3-1600 PC3-12800 DIMM Desktop Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('87846')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$52.05</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/128536s.jpg" border="0" width="150" height="75" title="HP 4GB DDR3L-1600 SODIMM Desktop Memory" alt="HP 4GB DDR3L-1600 SODIMM Desktop Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-4gb-ddr3l-1600-sodimm-desktop-a6-128536.htm">HP 4GB DDR3L-1600 SODIMM Desktop Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('128536')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$79.10</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/128537s.jpg" border="0" width="150" height="75" title="HP 8GB DDR3L-1600 SODIMM Desktop Memory" alt="HP 8GB DDR3L-1600 SODIMM Desktop Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/hp-8gb-ddr3l-1600-sodimm-desktop-81-128537.htm">HP 8GB DDR3L-1600 SODIMM Desktop Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('128537')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$134.81</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Kingston"></a>Kingston - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/95971s.jpg" border="0" width="150" height="75" title="Kingston HyperX Fury Memory Black 16GB 2x8GB DDR3-1866 CL10 Dual Channel Memory Kit" alt="Kingston HyperX Fury Memory Black 16GB 2x8GB DDR3-1866 CL10 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95971.htm">Kingston HyperX Fury Memory Black 16GB 2x8GB DDR3-1866 CL10 Dual Channel Memory Kit</a>
						<font size=1>(HX318C10FBK2/16)</font>
						

							
							
							
							
							

						
						
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('95971')" title="NCIX.com Real Time Stock Check"><font color="#669900">In&nbsp;Stock</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$167.19</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
					
					
					
					
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/96950s.jpg" border="0" width="150" height="75" title="Kingston 16GB 240-PIN DDR3 SDRAM DDR3 1866 (PC3 14900) ECC Registered Server Memory" alt="Kingston 16GB 240-PIN DDR3 SDRAM DDR3 1866 (PC3 14900) ECC Registered Server Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-16gb-240-pin-ddr3-sdram-a1-96950.htm?promoid=1374">Kingston 16GB 240-PIN DDR3 SDRAM DDR3 1866 (PC3 14900) ECC Registered Server Memory</a>
						<font size=1>(KVR18R13D4/16)</font>
						

							
							
							
							
							

						
						
						
						
							
							
						
						
					
						<br><font color="#CC0000">Save $70.99</font> off our regular price of $270.98
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('96950')" title="NCIX.com Real Time Stock Check"><font color="#669900">In&nbsp;Stock</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#cc0000" class="listing"><strong>$199.99</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/95956s.jpg" border="0" width="150" height="75" title="Kingston HyperX Fury Memory Black 8GB 2X4GB DDR3-1600 CL10 Dual Channel Memory Kit" alt="Kingston HyperX Fury Memory Black 8GB 2X4GB DDR3-1600 CL10 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95956.htm">Kingston HyperX Fury Memory Black 8GB 2X4GB DDR3-1600 CL10 Dual Channel Memory Kit</a>
						<font size=1>(HX316C10FBK2/8)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('95956')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$102.50</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/88613s.jpg" border="0" width="150" height="75" title="Kingston KVR16N11S8/4 4GB DDR3 1600MHz 240PIN DIMM Unbuff CL11 1.5V Gold Memory" alt="Kingston KVR16N11S8/4 4GB DDR3 1600MHz 240PIN DIMM Unbuff CL11 1.5V Gold Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-kvr16n11s8-4-4gb-ddr3-1600mhz-c7-88613.htm">Kingston KVR16N11S8/4 4GB DDR3 1600MHz 240PIN DIMM Unbuff CL11 1.5V Gold Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('88613')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$52.04</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/65772s.jpg" border="0" width="150" height="75" title="Kingston KVR1333D3N9/8G 8GB 1333MHz DDR3 NON-ECC CL9 DIMM" alt="Kingston KVR1333D3N9/8G 8GB 1333MHz DDR3 NON-ECC CL9 DIMM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-kvr1333d3n9-8g-8gb-1333mhz-ddr3-a9-65772.htm">Kingston KVR1333D3N9/8G 8GB 1333MHz DDR3 NON-ECC CL9 DIMM</a>
						<font size=1>(KVR1333D3N9/8G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('65772')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$84.99</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/88587s.jpg" border="0" width="150" height="75" title="Kingston KVR13N9S8K2/8 8GB 2x4GB Kits DDR3-1333MHZ DIMM Non-ECC Sr X8 CL9 Gold Single Rank Memory" alt="Kingston KVR13N9S8K2/8 8GB 2x4GB Kits DDR3-1333MHZ DIMM Non-ECC Sr X8 CL9 Gold Single Rank Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-kvr13n9s8k2-8-8gb-2x4gb-kits-6a-88587.htm">Kingston KVR13N9S8K2/8 8GB 2x4GB Kits DDR3-1333MHZ DIMM Non-ECC Sr X8 CL9 Gold Single Rank Memory</a>
						<font size=1>(KVR13N9S8K2/8)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('88587')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$86.51</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/95955s.jpg" border="0" width="150" height="75" title="Kingston HyperX Fury Memory Black 16GB 2X8GB DDR3-1600 CL10 Dual Channel Memory Kit" alt="Kingston HyperX Fury Memory Black 16GB 2X8GB DDR3-1600 CL10 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95955.htm">Kingston HyperX Fury Memory Black 16GB 2X8GB DDR3-1600 CL10 Dual Channel Memory Kit</a>
						<font size=1>(HX316C10FBK2/16)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('95955')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$220.66</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/95972s.jpg" border="0" width="150" height="75" title="Kingston HyperX Fury Memory Black 8GB 2x4GB DDR3-1866 CL10 Dual Channel Memory Kit" alt="Kingston HyperX Fury Memory Black 8GB 2x4GB DDR3-1866 CL10 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-hyperx-fury-memory-black-ed-95972.htm">Kingston HyperX Fury Memory Black 8GB 2x4GB DDR3-1866 CL10 Dual Channel Memory Kit</a>
						<font size=1>(HX318C10FBK2/8)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('95972')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$99.99</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/95977s.jpg" border="0" width="150" height="75" title="Kingston Hyperxfury Memory Red 16GB 2X8GB DDR3-1866 CL10 Dual Channel Memory Kit" alt="Kingston Hyperxfury Memory Red 16GB 2X8GB DDR3-1866 CL10 Dual Channel Memory Kit">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-hyperxfury-memory-red-16gb-78-95977.htm">Kingston Hyperxfury Memory Red 16GB 2X8GB DDR3-1866 CL10 Dual Channel Memory Kit</a>
						<font size=1>(HX318C10FRK2/16)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('95977')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$207.57</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/88582s.jpg" border="0" width="150" height="75" title="Kingston KVR13N9S8/4 4GB DDR3 1333MHz 240PIN DIMM Uunbuff CL9 1.5V Gold Sr X8 Memory" alt="Kingston KVR13N9S8/4 4GB DDR3 1333MHz 240PIN DIMM Uunbuff CL9 1.5V Gold Sr X8 Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-kvr13n9s8-4-4gb-ddr3-1333mhz-e7-88582.htm">Kingston KVR13N9S8/4 4GB DDR3 1333MHz 240PIN DIMM Uunbuff CL9 1.5V Gold Sr X8 Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('88582')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$67.06</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
				
				

			
			
				<tr>
					<td></td>
					
					<td colspan="3"><img src="/_img/btn_arrow.gif"  border="0"/> <a href="https://www.ncix.com/list/ddr3-memory-kingston-80-1303-98.htm" style="color:#000000">More <strong>Kingston</strong> DDR3 Memory</a></td>
				</tr>
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Kingston Branded"></a>Kingston Branded - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/129555s.jpg" border="0" width="150" height="75" title="Kingston 4GB DDR3 1600MHz Non-ECC CL11 1R X8 1.5V Unbuffered DIMM 240-PIN Memory" alt="Kingston 4GB DDR3 1600MHz Non-ECC CL11 1R X8 1.5V Unbuffered DIMM 240-PIN Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-4gb-ddr3-1600mhz-non-ecc-31-129555.htm">Kingston 4GB DDR3 1600MHz Non-ECC CL11 1R X8 1.5V Unbuffered DIMM 240-PIN Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('129555')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$65.80</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/129488s.jpg" border="0" width="150" height="75" title="Kingston 4GB DDR3 1333MHz Non-ECC CL9 1R X8 1.5V Unbuffered DIMM 240-PIN Memory" alt="Kingston 4GB DDR3 1333MHz Non-ECC CL9 1R X8 1.5V Unbuffered DIMM 240-PIN Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-4gb-ddr3-1333mhz-non-ecc-e1-129488.htm">Kingston 4GB DDR3 1333MHz Non-ECC CL9 1R X8 1.5V Unbuffered DIMM 240-PIN Memory</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('129488')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$65.39</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/121773s.jpg" border="0" width="150" height="75" title="Kingston 32GB Quad Rank LRDIMM 1600MHz DDR3L" alt="Kingston 32GB Quad Rank LRDIMM 1600MHz DDR3L">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-32gb-quad-rank-lrdimm-dd-121773.htm">Kingston 32GB Quad Rank LRDIMM 1600MHz DDR3L</a>
						<font size=1>(KTM-SX316LLQ/32G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('121773')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$745.40</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/117530s.jpg" border="0" width="150" height="75" title="Kingston 16GB 1866MHz Reg ECC Module DDR3" alt="Kingston 16GB 1866MHz Reg ECC Module DDR3">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-16gb-1866mhz-reg-ecc-70-117530.htm">Kingston 16GB 1866MHz Reg ECC Module DDR3</a>
						<font size=1>(KTH-PL318/16G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('117530')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$293.25</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/118302s.jpg" border="0" width="150" height="75" title="Kingston 4GB 1600MHz ECC Single Rank Module DDR3" alt="Kingston 4GB 1600MHz ECC Single Rank Module DDR3">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-4gb-1600mhz-ecc-single-08-118302.htm">Kingston 4GB 1600MHz ECC Single Rank Module DDR3</a>
						<font size=1>(KTD-PE316ES/4G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('118302')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$87.14</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/118714s.jpg" border="0" width="150" height="75" title="Kingston 8GB DDR3 1866MHz ECC DIMM HP" alt="Kingston 8GB DDR3 1866MHz ECC DIMM HP">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/kingston-8gb-ddr3-1866mhz-ecc-70-118714.htm">Kingston 8GB DDR3 1866MHz ECC DIMM HP</a>
						<font size=1>(KTH-PL318E/8G)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('118714')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$129.98</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Lenovo"></a>Lenovo - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/104994s.jpg" border="0" width="150" height="75" title="Lenovo 4GB DDR3 1600 PC3-12800 UDIMM Memory for ThinkCentre Small Form Factor and Tower Desktop" alt="Lenovo 4GB DDR3 1600 PC3-12800 UDIMM Memory for ThinkCentre Small Form Factor and Tower Desktop">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/lenovo-4gb-ddr3-1600-pc3-12800-53-104994.htm">Lenovo 4GB DDR3 1600 PC3-12800 UDIMM Memory for ThinkCentre Small Form Factor and Tower Desktop</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('104994')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$84.49</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/images/space.gif" border="0" width="150" height="75" title="LENOVO 32GB PC3L-10600 CL9 ECC DDR3 1333MHZ LP SDRAM" alt="LENOVO 32GB PC3L-10600 CL9 ECC DDR3 1333MHZ LP SDRAM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/lenovo-32gb-pc3l-10600-cl9-ecc-02-131667.htm">LENOVO 32GB PC3L-10600 CL9 ECC DDR3 1333MHZ LP SDRAM</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('131667')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$1,456.32</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="Micron"></a>Micron - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/images/space.gif" border="0" width="150" height="75" title="MICRON 16GB PC3-12800 1600MHZ DDR3" alt="MICRON 16GB PC3-12800 1600MHZ DDR3">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/micron-16gb-pc3-12800-1600mhz-ddr3-d8-114676.htm">MICRON 16GB PC3-12800 1600MHZ DDR3</a>
						<font size=1>(CT16G3ERSLD4160B)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('114676')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$185.84</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="QNAP Inc."></a>QNAP Inc. - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
				
				
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/119393s.jpg" border="0" width="150" height="75" title="QNAP 8GB DDR3 ECC RAM for TS-EC879U/EC1279U/EC1679U &amp; SAS Series" alt="QNAP 8GB DDR3 ECC RAM for TS-EC879U/EC1279U/EC1679U &amp; SAS Series">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/qnap-8gb-ddr3-ecc-ram-8e-119393.htm">QNAP 8GB DDR3 ECC RAM for TS-EC879U/EC1279U/EC1679U & SAS Series</a>
						<font size=1>(RAM-8GDR3EC-LD-1600)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('119393')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$269.34</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="SuperMicro"></a>SuperMicro - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/gif/113974s.jpg" border="0" width="150" height="75" title="Supermicro MEM-DR380L-HL03-UN16 8GB DDR3-1600 2RX8 Non-ECC Unbuffered DIMM Server Memory" alt="Supermicro MEM-DR380L-HL03-UN16 8GB DDR3-1600 2RX8 Non-ECC Unbuffered DIMM Server Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/supermicro-mem-dr380l-hl03-un16-8gb-ddr3-1600-2rx8-a3-113974.htm">Supermicro MEM-DR380L-HL03-UN16 8GB DDR3-1600 2RX8 Non-ECC Unbuffered DIMM Server Memory</a>
						<font size=1>(MEM-DR380L-HL03-UN16)</font>
						

							
							
							
							
							

						
						
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('113974')" title="NCIX.com Real Time Stock Check"><font color="#669900">In&nbsp;Stock</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$149.98</strong>
						
					
				</td>
				
			</tr>
			

			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://content.etilize.com/Large/1039142374.jpg" border="0" width="150" height="75" title="Supermicro MEM-DR380L-HL03-SO16 8GB DDR3-1600 Server Memory" alt="Supermicro MEM-DR380L-HL03-SO16 8GB DDR3-1600 Server Memory">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/supermicro-mem-dr380l-hl03-so16-8gb-ddr3-1600-server-b9-143221.htm">Supermicro MEM-DR380L-HL03-SO16 8GB DDR3-1600 Server Memory</a>
						<font size=1>(MEM-DR380L-HL03-SO16)</font>
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('143221')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$169.99</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
			<TR>
				<TD colspan="3" align="left"><h2><font color="#CC0000" size="3"><strong><br><a name="VISIONTEK"></a>VISIONTEK - DDR3 Memory</strong></font></h2></TD>
				<TD valign="bottom" align="right"><a href="#mtop"><img src="https://d1sfu4378rr01a.cloudfront.net/_img/top_link.gif" border="0"></a></TD>
			</TR>
			<tr align="left" valign="top" class="listing" bgcolor="#CCCCCC">
				<td class="linehead"><font color="#666666"><strong>Part&nbsp;#</strong></font></td>
				<td class="linehead"><font color="#666666"><strong>Description</strong></font></td>
				<td class="linehead" align="center"><font color="#666666"><strong>Avail</strong></font></td>
				<td class="linehead" align="right"><font color="#666666"><strong>Price</strong></font></td>
				
			</tr>
			
			
			
			
				
				

				
				
				
				
				
				
			
			
			
			
			
			
			
			<tr valign="top">
				<td class="line" width="150">
					<img src="https://d1sfu4378rr01a.cloudfront.net/images/space.gif" border="0" width="150" height="75" title="Visiontek 8GB DDR3 PC3-12800 CL11 1600 SDRAM" alt="Visiontek 8GB DDR3 PC3-12800 CL11 1600 SDRAM">
					
				</td>
				<td class="line" align="left">
					<span class="listing">
						<a href="https://www.ncix.com/detail/visiontek-8gb-ddr3-pc3-12800-cl11-80-126314.htm">Visiontek 8GB DDR3 PC3-12800 CL11 1600 SDRAM</a>
						
						

							
							
							
							
							

						
						
						
							
							
							
							Back Order
						
						
							
							
						
						
					

					</span>
				</td>
				<td class="line" align="center" nowrap="nowrap">
					<b><a href="javascript:checkinventory('126314')" title="NCIX.com Real Time Stock Check"><font color="#669900">***</font></a></b>
				</td>
				<td class="line" align="right" nowrap>
					
						<font color="#333333" class="listing"><strong>$94.44</strong>
						
					
				</td>
				
			</tr>
			

			
			

		
		</table>

<!--cend-->
</div>
</div>
<script language="JavaScript">
	var isopen		=	0;
	var lsku		=	"";
	var mywindow;
	function checkinventory(sku){
		width		=	650;
		height		=	400;
		xposition	=	0;
		yposition	=	0;
		xposition	= (screen.width - width) / 2;
		yposition	= (screen.height - height) / 2;
		args= "width=" + width + ","
		+ "height=" + height + ","
		+ "location=0,"
		+ "menubar=0,"
		+ "resizable=0"
		+ ",scrollbars=1,"
		+ "status=0,"
		+ "titlebar=0,"
		+ "toolbar=0,"
		+ "hotkeys=0,"
		+ "screenx=" + xposition + "," //NN Only
		+ "screeny=" + yposition + "," //NN Only
		+ "left=" + xposition + "," //IE Only
		+ "top=" + yposition; //IE Only
		if(typeof(mywindow) =='object'){
			mywindow.close();
		}
		if(lsku == sku){
			lsku	=	"";
		}else{
			lsku		=	sku;
			mywindow	=	window.open( 'https://ajax.ncix.com/checkinventory.php?sku='+sku,'realtimecheck',args );
		}
	}
</script>


<input name="minorcatid" type="hidden" id="minorcatid" value="1303" />
<input name="subminorcatid"  type="hidden" id="subminorcatid" value="" />

<script language="JavaScript">
	
		document.writeln("<img src='https://ajax.ncix.com/clickrecord.php?minorcatid=1303'>");
	
</script>

<script type="text/javascript">
var google_tag_params = {
ecomm_prodid: : '',
ecomm_pagetype: 'category',
ecomm_totalvalue: ''
};
</script>




<div id="categorypage"></div>

	
	
		
			
			
		
	
		
			
				
			
			
		
	
		
			
				
			
			
		
	
		
	
		
	
		
	
		
	
		
	
		
	
		
	
		
	
		
	
	<script type="text/javascript" src="//static.criteo.net/js/ld/ld.js" async="true"></script>
	<script type="text/javascript">
	window.criteo_q = window.criteo_q || [];
	var deviceType=
	/iPad/.test(navigator.userAgent)?"t":/Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Silk/.test(navigator.
	userAgent)?"m":"d";
	window.criteo_q.push(
	{ event: "setAccount", account: 21749},
	{ event: "setSiteType", type: deviceType},
	{ event: "setHashedEmail", email: [""]},
	{ event: "viewList", item: ["66354","73133","96950"] });
	</script>



	
			
	


	
		<div style="clear:both;"></div>
		

<div style="margin-top:30px; margin-left:20px; margin-bottom:30px;">
	<div><h3>
	
	 
	 Top 5 most recent reviews on <font color="#cc3300">DDR3 Memory</font>
	 
	
	</h3>
	</div>
	
		
		
		
		
			
			<table border="0" width="100%" cellpadding="4" cellspacing="0" style="padding-left:10px; border:1px solid #ddd; margin-top:20px;">
				
					
					
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
							
					<tr>
						<td colspan="2"><h3>Customer Review of <a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-73133.htm">G.SKILL Ripjaws X 16GB (2x8GB) DDR3-1600 CL10-10-10-30 1.5V 240PIN Dual Channel Memory Kit - Red</a></h3></td>
					</tr>
					<tr valign="top">
						<td width="20%"><strong>Anderson_Y</strong><br /> 11/23/17<br /> Experience: 2 Years<br /></td>
						<td>
							<table width="100%" border="0" cellpadding="2" cellspacing="0">
								<tr valign="top" >
									<td width="100px" height="32" ><img src="https://source.ncix.com/Review-stars/images1/img_stars_5.gif" /></td><td valign="top"></td>
									<td align="right" height="32"  style="padding-right:15px;" >
										<div id="div259517" style="display:none"> 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/tips.cfm?product_id=73133&reviewid=259517','',300,300,1,0)">Tip this Review</a> | 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/reviewreport.cfm?id=259517','',300,300,1,0)" style="margin-right:15px">Flag this Review</a>
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/productreviewlike.cfm?id=259517','',300,300,1,0)"><img  align="texttop" src="https://source.ncix.com/bnr/site_assets/like.gif" alt="link" name="like_thumbs" border="0" id="like_thumbs" /></a>
										(+5)
										</div>
									</td>
								</tr>
							</table>
							<table cellpadding="4">
								<tr>
									<td>
										<div style="font-weight:bold">Summary</div>
										<span class="normal_text2">
										
											
											Looks good and great heat sinks spreaders
											
										
										<a href="https://www.ncix.com/products/?mode=productreviewread&product_id=73133" style="color:blue">&raquo; Read More About  G.SKILL Ripjaws X 16GB (2x8GB)</a>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					
				
			</table>
			
		


		
		
		
		
			
			<table border="0" width="100%" cellpadding="4" cellspacing="0" style="padding-left:10px; border:1px solid #ddd; margin-top:20px;">
				
					
					
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
							
					<tr>
						<td colspan="2"><h3>Customer Review of <a href="https://www.ncix.com/detail/g-skill-ripjaws-x-16gb-2x8gb-a3-104837.htm">G.SKILL Ripjaws X 16GB (2x8GB) DDR3-2133 CL11-13-13-31 1.5V 240PIN Dual Channel Memory Kit - Red</a></h3></td>
					</tr>
					<tr valign="top">
						<td width="20%"><strong>yan_z</strong><br /> 10/30/17<br /> Experience: 2 Years<br /></td>
						<td>
							<table width="100%" border="0" cellpadding="2" cellspacing="0">
								<tr valign="top" >
									<td width="100px" height="32" ><img src="https://source.ncix.com/Review-stars/images1/img_stars_5.gif" /></td><td valign="top"></td>
									<td align="right" height="32"  style="padding-right:15px;" >
										<div id="div259358" style="display:none"> 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/tips.cfm?product_id=104837&reviewid=259358','',300,300,1,0)">Tip this Review</a> | 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/reviewreport.cfm?id=259358','',300,300,1,0)" style="margin-right:15px">Flag this Review</a>
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/productreviewlike.cfm?id=259358','',300,300,1,0)"><img  align="texttop" src="https://source.ncix.com/bnr/site_assets/like.gif" alt="link" name="like_thumbs" border="0" id="like_thumbs" /></a>
										(+3)
										</div>
									</td>
								</tr>
							</table>
							<table cellpadding="4">
								<tr>
									<td>
										<div style="font-weight:bold">Summary</div>
										<span class="normal_text2">
										
											
											during my two year of using this, it does not burned out or broken. highly recommended
											
										
										<a href="https://www.ncix.com/products/?mode=productreviewread&product_id=104837" style="color:blue">&raquo; Read More About  G.SKILL Ripjaws X 16GB (2x8GB)</a>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					
				
			</table>
			
		


		
		
		
		
			
			<table border="0" width="100%" cellpadding="4" cellspacing="0" style="padding-left:10px; border:1px solid #ddd; margin-top:20px;">
				
					
					
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
							
					<tr>
						<td colspan="2"><h3>Customer Review of <a href="https://www.ncix.com/detail/g-skill-ripjaws-x-8gb-2x4gb-01-57953.htm">G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1600 CL9-9-9-24 1.5V 240PIN Dual Channel Memory Kit - Red</a></h3></td>
					</tr>
					<tr valign="top">
						<td width="20%"><strong>turbotime</strong><br /> 10/27/17<br /> Experience: 3 Years<br /></td>
						<td>
							<table width="100%" border="0" cellpadding="2" cellspacing="0">
								<tr valign="top" >
									<td width="100px" height="32" ><img src="https://source.ncix.com/Review-stars/images1/img_stars_5.gif" /></td><td valign="top"></td>
									<td align="right" height="32"  style="padding-right:15px;" >
										<div id="div259344" style="display:none"> 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/tips.cfm?product_id=57953&reviewid=259344','',300,300,1,0)">Tip this Review</a> | 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/reviewreport.cfm?id=259344','',300,300,1,0)" style="margin-right:15px">Flag this Review</a>
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/productreviewlike.cfm?id=259344','',300,300,1,0)"><img  align="texttop" src="https://source.ncix.com/bnr/site_assets/like.gif" alt="link" name="like_thumbs" border="0" id="like_thumbs" /></a>
										(+5)
										</div>
									</td>
								</tr>
							</table>
							<table cellpadding="4">
								<tr>
									<td>
										<div style="font-weight:bold">Summary</div>
										<span class="normal_text2">
										
											
											Great!
											
										
										<a href="https://www.ncix.com/products/?mode=productreviewread&product_id=57953" style="color:blue">&raquo; Read More About  G.SKILL Ripjaws X 8GB (2x4GB)</a>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					
				
			</table>
			
		


		
		
		
		
			
			<table border="0" width="100%" cellpadding="4" cellspacing="0" style="padding-left:10px; border:1px solid #ddd; margin-top:20px;">
				
					
					
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
							
					<tr>
						<td colspan="2"><h3>Customer Review of <a href="https://www.ncix.com/detail/g-skill-ripjaws-x-8gb-2x4gb-01-58519.htm">G.SKILL Ripjaws X 8GB (2x4GB) DDR3-1866 CL9-10-9-28 1.5V 240PIN Dual Channel Memory Kit - Red</a></h3></td>
					</tr>
					<tr valign="top">
						<td width="20%"><strong>Mathieu_L8</strong><br /> 09/06/17<br /> Experience: 3 Days<br /></td>
						<td>
							<table width="100%" border="0" cellpadding="2" cellspacing="0">
								<tr valign="top" >
									<td width="100px" height="32" ><img src="https://source.ncix.com/Review-stars/images1/img_stars_5.gif" /></td><td valign="top"><img src="https://source.ncix.com/bnr/site_assets/checkmark.png" />&nbsp;Verified Owner</td>
									<td align="right" height="32"  style="padding-right:15px;" >
										<div id="div259118" style="display:none"> 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/tips.cfm?product_id=58519&reviewid=259118','',300,300,1,0)">Tip this Review</a> | 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/reviewreport.cfm?id=259118','',300,300,1,0)" style="margin-right:15px">Flag this Review</a>
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/productreviewlike.cfm?id=259118','',300,300,1,0)"><img  align="texttop" src="https://source.ncix.com/bnr/site_assets/like.gif" alt="link" name="like_thumbs" border="0" id="like_thumbs" /></a>
										(+3)
										</div>
									</td>
								</tr>
							</table>
							<table cellpadding="4">
								<tr>
									<td>
										<div style="font-weight:bold">Summary</div>
										<span class="normal_text2">
										
											
											I've been buying g.skills for all my build for the last 5 years and never had any issues with all of them. These one included. It is very reliable and has very good performance. 
											
										
										<a href="https://www.ncix.com/products/?mode=productreviewread&product_id=58519" style="color:blue">&raquo; Read More About  G.SKILL Ripjaws X 8GB (2x4GB)</a>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					
				
			</table>
			
		


		
		
		
		
			
			<table border="0" width="100%" cellpadding="4" cellspacing="0" style="padding-left:10px; border:1px solid #ddd; margin-top:20px;">
				
					
					
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
						
						
					
						
							
					<tr>
						<td colspan="2"><h3>Customer Review of <a href="https://www.ncix.com/detail/corsair-vengeance-blue-cmz8gx3m2a1600c9b-8gb-5d-59431.htm">Corsair Vengeance Blue CMZ8GX3M2A1600C9B 8GB 2x4GB DDR3-1600 CL9-9-9-24 Dual Channel Memory Kit</a></h3></td>
					</tr>
					<tr valign="top">
						<td width="20%"><strong>David_H73</strong><br /> 07/27/17<br /> Experience: 5 Years<br /></td>
						<td>
							<table width="100%" border="0" cellpadding="2" cellspacing="0">
								<tr valign="top" >
									<td width="100px" height="32" ><img src="https://source.ncix.com/Review-stars/images1/img_stars_5.gif" /></td><td valign="top"><img src="https://source.ncix.com/bnr/site_assets/checkmark.png" />&nbsp;Verified Owner</td>
									<td align="right" height="32"  style="padding-right:15px;" >
										<div id="div258843" style="display:none"> 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/tips.cfm?product_id=59431&reviewid=258843','',300,300,1,0)">Tip this Review</a> | 
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/reviewreport.cfm?id=258843','',300,300,1,0)" style="margin-right:15px">Flag this Review</a>
										<a href="javascript:openNewWindow('https://secure1.ncix.com/products/productreviewlike.cfm?id=258843','',300,300,1,0)"><img  align="texttop" src="https://source.ncix.com/bnr/site_assets/like.gif" alt="link" name="like_thumbs" border="0" id="like_thumbs" /></a>
										(+5)
										</div>
									</td>
								</tr>
							</table>
							<table cellpadding="4">
								<tr>
									<td>
										<div style="font-weight:bold">Summary</div>
										<span class="normal_text2">
										
											
											I bought the 16 gb kit 5 years ago. A module went bad. I am glad it is still available!!!
											
										
										<a href="https://www.ncix.com/products/?mode=productreviewread&product_id=59431" style="color:blue">&raquo; Read More About  Corsair Vengeance Blue CMZ8GX3M2A1600C9B 8GB</a>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					
				
			</table>
			
		


</div>
		

				
					
		</td>
	</tr>
</table>
<br/><br/>&nbsp;

					
					
						






	






	




	
		
		





	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
			
				
			
			
						
			
		
		
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
			
				
			
			
						
			
		
		
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

					
					
				</td>
				
						<Td width="167" class="sm-right" valign="top">





<table border=0 cellpadding="3" cellspacing="0" width="165">
	
	<tr>
		<td background="/_img/_dot.gif" valign="top">
			
			
			
				






	






	




	
		
		





	
	
	


	
	

	
		
			
	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
			
				
			
			
				
					
				
			
		
		
	

	

	
	
	
		
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
		
	


	
	
		
			
			
			
						
			
		
		
	

	
		
			
	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	
		
			
			
				
			
			
						
			
		
		
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
					
		
	


	
	
		
			
			
				
			
			
						
			
		
		
	

	
		
		
			
				
					
						<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "https://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script>
$(document).ready(function() {
$('#frmSS5').submit(function()
{
window.open('', '.formpopup', 'width=850,height=300');
this.target = '.formpopup';
});
});
</script>
<SCRIPT type="text/javascript">
var dhtmlgoodies_tooltip = false;
var dhtmlgoodies_tooltipShadow = false;
var dhtmlgoodies_shadowSize = 4;
var dhtmlgoodies_tooltipMaxWidth = 300;
var dhtmlgoodies_tooltipMinWidth = 100;
var dhtmlgoodies_iframe = false;
var tooltip_is_msie = (navigator.userAgent.indexOf('MSIE')>=0 && navigator.userAgent.indexOf('opera')==-1 && document.all)?true:false;
function showTooltip(e,tooltipTxt)
{
var bodyWidth = Math.max(document.body.clientWidth,document.documentElement.clientWidth) - 20;
if(!dhtmlgoodies_tooltip){
dhtmlgoodies_tooltip = document.createElement('DIV');
dhtmlgoodies_tooltip.id = 'dhtmlgoodies_tooltip';
dhtmlgoodies_tooltipShadow = document.createElement('DIV');
dhtmlgoodies_tooltipShadow.id = 'dhtmlgoodies_tooltipShadow';
document.body.appendChild(dhtmlgoodies_tooltip);
document.body.appendChild(dhtmlgoodies_tooltipShadow);
if(tooltip_is_msie){
dhtmlgoodies_iframe = document.createElement('IFRAME');
dhtmlgoodies_iframe.frameborder='5';
dhtmlgoodies_iframe.style.backgroundColor='#FFFFFF';
dhtmlgoodies_iframe.src = '#';
dhtmlgoodies_iframe.style.zIndex = 100;
dhtmlgoodies_iframe.style.position = 'absolute';
document.body.appendChild(dhtmlgoodies_iframe);
}
}
dhtmlgoodies_tooltip.style.display='block';
dhtmlgoodies_tooltipShadow.style.display='block';
if(tooltip_is_msie)dhtmlgoodies_iframe.style.display='block';
var st = Math.max(document.body.scrollTop,document.documentElement.scrollTop);
if(navigator.userAgent.toLowerCase().indexOf('safari')>=0)st=0;
var leftPos = e.clientX + 10;
dhtmlgoodies_tooltip.style.width = null;	// Reset style width if it's set
dhtmlgoodies_tooltip.innerHTML = tooltipTxt;
dhtmlgoodies_tooltip.style.left = leftPos + 'px';
dhtmlgoodies_tooltip.style.top = e.clientY + 10 + st + 'px';
dhtmlgoodies_tooltipShadow.style.left = leftPos + dhtmlgoodies_shadowSize + 'px';
dhtmlgoodies_tooltipShadow.style.top = e.clientY + 10 + st + dhtmlgoodies_shadowSize + 'px';
if(dhtmlgoodies_tooltip.offsetWidth>dhtmlgoodies_tooltipMaxWidth){	/* Exceeding max width of tooltip ? */
dhtmlgoodies_tooltip.style.width = dhtmlgoodies_tooltipMaxWidth + 'px';
}
var tooltipWidth = dhtmlgoodies_tooltip.offsetWidth;
if(tooltipWidth<dhtmlgoodies_tooltipMinWidth)tooltipWidth = dhtmlgoodies_tooltipMinWidth;
dhtmlgoodies_tooltip.style.width = tooltipWidth + 'px';
dhtmlgoodies_tooltipShadow.style.width = dhtmlgoodies_tooltip.offsetWidth + 'px';
dhtmlgoodies_tooltipShadow.style.height = dhtmlgoodies_tooltip.offsetHeight + 'px';
if((leftPos + tooltipWidth)>bodyWidth){
dhtmlgoodies_tooltip.style.left = (dhtmlgoodies_tooltipShadow.style.left.replace('px','') - ((leftPos + tooltipWidth)-bodyWidth)) + 'px';
dhtmlgoodies_tooltipShadow.style.left = (dhtmlgoodies_tooltipShadow.style.left.replace('px','') - ((leftPos + tooltipWidth)-bodyWidth) + dhtmlgoodies_shadowSize) + 'px';
}
if(tooltip_is_msie){
dhtmlgoodies_iframe.style.left = dhtmlgoodies_tooltip.style.left;
dhtmlgoodies_iframe.style.top = dhtmlgoodies_tooltip.style.top;
dhtmlgoodies_iframe.style.width = dhtmlgoodies_tooltip.offsetWidth + 'px';
dhtmlgoodies_iframe.style.height = dhtmlgoodies_tooltip.offsetHeight + 'px';
}
}
function hideTooltip()
{
dhtmlgoodies_tooltip.style.display='none';
dhtmlgoodies_tooltipShadow.style.display='none';
if(tooltip_is_msie)dhtmlgoodies_iframe.style.display='none';
}
</SCRIPT>
<script type="text/javascript">
function LocationUpdate(f)
{
var location = f.value;
var locupdate = document.getElementById("CustomFields_20_5");
if (location != "")
{
locupdate.value = "Yes";
}
if (location == "")
{
locupdate.value = "No";
}
}
</script>
<style>
#newsletter-bg
{
background: rgba(255,255,255,1);
background: -moz-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(255,255,255,1)), color-stop(47%, rgba(246,246,246,1)), color-stop(100%, rgba(227,227,227,1)));
background: -webkit-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: -o-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: -ms-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#e3e3e3', GradientType=0 );
}
</style>
<script type='text/javascript'>
var googletag = googletag || {};
googletag.cmd = googletag.cmd || [];
(function() {
var gads = document.createElement('script');
gads.async = true;
gads.type = 'text/javascript';
var useSSL = 'https:' == document.location.protocol;
gads.src = (useSSL ? 'https:' : 'https:') +
'//www.googletagservices.com/tag/js/gpt.js';
var node = document.getElementsByTagName('script')[0];
node.parentNode.insertBefore(gads, node);
})();
</script>
<script type='text/javascript'>
googletag.cmd.push(function() {
googletag.defineSlot('/4538120/NCIX_Weekly_Side', [160, 300], 'div-gpt-ad-1447893447894-0').addService(googletag.pubads());
googletag.pubads().enableSingleRequest();
googletag.pubads().collapseEmptyDivs();
googletag.enableServices();
});
</script>
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,600,800' rel='stylesheet' type='text/css'>
<table width="160" align="right" border="0" cellpadding="0" cellspacing="0">
<tr>
<td>
<table width="160" align="right" border="0" cellpadding="0" cellspacing="0" style="margin-bottom:2px;">
<tr><td height="6" colspan="5"></td></tr>
<tr>
<td><font face="Verdana, Geneva, sans-serif" size="1">Connect:</font></td>
<td><a href="https://www.youtube.com/user/NCIXcom"><img src="https://dhsj95t7aazhx.cloudfront.net/social-icons/Youtube-mini-icon.gif" alt="NCIX Youtube icon" border="0"></a></td>
<td><a href="https://www.facebook.com/NCIXdotCOM"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/footer_social/facebook.gif" alt="NCIX Facebook icon" border="0"></a></td>
<td><a href="https://www.instagram.com/ncixdotcom/"><img src="https://dhsj95t7aazhx.cloudfront.net/social-icons/Instagram-mini-icon.gif" alt="NCIX Instagram icon" border="0"></a></td>
<td><a href="https://twitter.com/NCIXdotCOM"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/footer_social/twitter.gif" border="0"></a></td>
<!--
<td><a href="https://plus.google.com/101746540581038237777"><img src="
https://dhsj95t7aazhx.cloudfront.net/bnr/footer_social/google.gif" alt="NCIX Google+ icon" border="0"></a></td>-->
</tr>
</table>
</td>
</tr>
<tr><td height="6"></td></tr>
<tr>
<td>
<!-- Start ASPM
<table width="160" align="right" border="0" cellpadding="0" cellspacing="0" style="margin-bottom:2px;">
<tr><td height="1"><img src="https://dhsj95t7aazhx.cloudfront.net/aspm/line.gif" style="padding-bottom:2px;"></td></tr>
<tr><td align="center">
<div style="padding-bottom:2px;">
<a href="https://www.ncix.com/article/ASPM-Advanced-Store-Price-Match.htm">
<img src="https://dhsj95t7aazhx.cloudfront.net/aspm/aspm-right-side.gif" border="0" alt="NCIX Advanced Store Price Match logo"></a>
</div>
<font face="Verdana, Geneva, sans-serif" size="1" style="color:#000; text-decoration:none;">Advanced Store Price Match</font>
</td>
</tr>
<tr><td height="1"><img src="https://dhsj95t7aazhx.cloudfront.net/aspm/line.gif" style=" padding:4px 0 0px 0;"></td></tr>
</table>
<!-- End ASPM -->
</td>
</tr>
<tr><td height="6"></td></tr>
<tr>
<td>
<!-- Latest Eblast -->
<div id="subscribebox" style="width:160px;">
<div id="form">
<!-- Subscribe FORM -->
<table width="160px" border="0" cellpadding="0" cellspacing="0" align="right">
<tr>
<td><a href="https://dhsj95t7aazhx.cloudfront.net/eblast-1129/index-ca-web.html" target="_new"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/latest-eblast/view-latest.jpg" alt="Latest eblast" width="160" border="0" style="display:block"></a>
</td>
</tr>
<tr> <td height="8px"></td></tr>
<tr> <td style="border-top:2px dotted #e3e3e3;""></td></tr>
<tr>
<td bgcolor="#FFF" width="160" id="newsletter-bg" style="max-width:160px;" align="center">
<!--Start Socketlabs opt-in signup form. See https://support.socketlabs.com/kb/166 for more information-->
<link href="https://dhsj95t7aazhx.cloudfront.net/NCIX-Newsletter-Signup/CSS-newsletter2.css" type="text/css" rel="stylesheet"/>
<style>
/*Your custom styles here*/
#newsletter-bg {
background: rgba(255,255,255,1);
background: -moz-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: -webkit-gradient(left top, left bottom, color-stop(0%, rgba(255,255,255,1)), color-stop(47%, rgba(246,246,246,1)), color-stop(100%, rgba(227,227,227,1)));
background: -webkit-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: -o-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: -ms-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
background: linear-gradient(to bottom, rgba(255,255,255,1) 0%, rgba(246,246,246,1) 47%, rgba(227,227,227,1) 100%);
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#e3e3e3', GradientType=0 );
}
</style>
<noscript>
<div align="center" style="font-family:'Open Sans', sans-serif;font-size:12px; color:#111; font-weight:300; line-height:16px;text-align:center; padding-top:7px; ">
<!-- To enable this sign up form, please enable javascript on your browser. -->
<a href="https://www.ncix.com/newsletters/">
<img src="https://dhsj95t7aazhx.cloudfront.net/ncix-graphics/images/SignMeUp-Btn.png" border="0" width="142px" /></a>
</div></noscript>
<!--
Additional attributes. These additional attributes only apply if the form is a modal form. i.e. data-sl-show-modal is set to a value >= 0
- data-sl-dismissed-timer -The number of minutes to not show a form, (on page load), after a form has been dismissed.
- data-sl-show-after-completed -true/false indicating that the form should continue to show, (on page load), even after it has been completed.
-->
<div style="font-family:'Open Sans', sans-serif;font-size:16px; color:#111; font-weight:400; line-height:18px; padding:8px 0 0 0; margin:0 auto; text-align:center; ">
Get Deal Alerts in your Inbox!
</div>
<div style="font-family:'Open Sans', sans-serif;font-size:12px; color:#111; font-weight:300; line-height:16px;text-align:center; padding-top:7px;">
Don't miss out on the latest coupons and rewards.
</div>
<center>
<br />
<div class="createsend-button" style="height:27px;display:inline-block; width:155px; max-width:156px;" data-listid="d/98/D83/201/C74C1BF3A4D62E8B">
</div><script type="text/javascript">(function () { var e = document.createElement('script'); e.type = 'text/javascript'; e.async = true; e.src = ('https:' == document.location.protocol ? 'https' : 'http') + '://btn.createsend1.com/js/sb.min.js?v=3'; e.className = 'createsend-script'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(e, s); })();</script>
</center>
<!--End Socketlabs opt-in signup form-->
<div style="padding:5px 5px 10px 5px; font-family: 'Open Sans', sans-serif; font-size:9px; font-weight:400; line-height:12px; color:#666; text-align:center;">
Please read our <br><a href="https://www.ncix.com/privacy/">privacy policy</a> for details.
</div>
</td></tr></table>
<!-- END Subscribe FORM -->
</div>
</div>
<!-- End Latest Eblast -->
</td>
</tr>
<tr><td height="4"></td></tr>
<tr>
<td>
<table cellspacing="0" cellpadding="0">
<!-- Weekend header--><!--
<tr><td height="2"></td></tr>
<tr>
<td>
<a href="https://www.ncix.com/subpromo/1382.htm">
<img src="https://dhsj95t7aazhx.cloudfront.net/eblast12-01/Side-160x300.jpg" alt="NCIX Weekend Sale banner" border="0" onClick="ga('send', 'event', 'RHS Link', 'RHS - WeekendSaleDec1', 'WeekendSaleDec1');"></a>
</td>
</tr>
<tr><td height="4"></td></tr>
<!---->
<tr>
<td>
<a href="https://www.ncix.com/promo/HolidayJumpstart2017.htm">
<img src="https://dhsj95t7aazhx.cloudfront.net/ws/HolidayJumpstart2017-160w.jpg?3" alt="NCIX Sale banner" border="0" onClick="ga('send', 'event', 'RHS Link', 'RHS - HolidayJumpstart 2017', 'HolidayJumpstart 2017');"></a>
</td>
</tr>
<!----->
<tr><td height="4"></td></tr>
</table>
</td>
</tr>
</table>
<!--
</td>
</tr>
</table>
-->
					
					<span style="display:none">Contentname:biz_Home_Vertical_StoreWeekly</span>
				
					
						<!DOCTYPE HTML>
<html lang="en-us">
<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8">

<style type="text/css" media="screen">
</style>
<script type='text/javascript' src='https://partner.googleadservices.com/gampad/google_service.js'>
</script>
<script type='text/javascript'>
GS_googleAddAdSenseService("ca-pub-9043224176482471");
GS_googleEnableAllServices();
</script>
<script type='text/javascript'>
GA_googleAddSlot("ca-pub-9043224176482471", "NCIX-FeaturedRotational");
</script>
<script type='text/javascript'>
GA_googleFetchAds();
</script>
</head>
<!-- NCIX-FeaturedRotational -->
<script type='text/javascript'>
GA_googleFillSlot("NCIX-FeaturedRotational");
</script>
					
					<span style="display:none">Contentname:NCIX-featured-rotational</span>
				
					
						<table width="160px" border="0" cellpadding="0" cellspacing="0" align="right">
<tr><td>
<script type='text/javascript' src='https://partner.googleadservices.com/gampad/google_service.js'>
</script>
<script type='text/javascript'>
GS_googleAddAdSenseService("ca-pub-9043224176482471");
GS_googleEnableAllServices();
</script>
<script type='text/javascript'>
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_160x300_AU");
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_Tier1_AU_B");
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_Tier1_AU_C");
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_Tier1_AU_D");
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_Tier2_AU");
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_Tier2_AU_B");
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_Tier2_AU_C");
GA_googleAddSlot("ca-pub-9043224176482471", "BTS_Tier2_AU_D");
</script>
<script type='text/javascript'>
GA_googleFetchAds();
</script>
<table align="center" cellspacing="0" cellpadding="0">
<tr><td>
<!-- BTS_160x300_AU -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_160x300_AU");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<tr><td>
<!-- BTS_Tier1_AU_B -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_Tier1_AU_B");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<tr><td>
<!-- BTS_Tier1_AU_B -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_Tier1_AU_C");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<tr><td>
<!-- BTS_Tier1_AU_B -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_Tier1_AU_D");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<tr><td>
<!-- BTS_Tier2_AU -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_Tier2_AU");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<tr><td>
<!-- BTS_Tier2_AU_B -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_Tier2_AU_B");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<tr><td>
<!-- BTS_Tier2_AU_C -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_Tier2_AU_C");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<tr><td>
<!-- BTS_Tier2_AU_D -->
<script type='text/javascript'>
GA_googleFillSlot("BTS_Tier2_AU_D");
</script>
</td></tr>
<tr><td height="4"></td></tr>
<!--
<tr><td><a href="https://dhsj95t7aazhx.cloudfront.net/eblast/Weekly-eblast-20130904/index-caweb.html?1"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/dept_ad/ad_serve/other/images/newsletter_01.jpg" border="0"></a></td></tr>
<tr><td><a href="https://www.ncix.com/newsletters/"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/dept_ad/ad_serve/other/images/newsletter_02.jpg" border="0"></a></td></tr>
-->
</table>
</td></tr></table>
					
					<span style="display:none">Contentname:160x300_Tier</span>
							
			
			
	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	


	
	

	
		
			
	

	
	
	


	
	

	
		
			
	

	
	
	


	
	

	
		
			
	

	
	
	
		
		
			
		
		
			
				
			
		
	


	
	

	

	
	
	


	
	

	
		
			
	

	
	
	


	
	

	
		
			
	

			
			
			
			
			&nbsp;
		</td>
	</tr>
</table>
</td>
				
			</tr>
		</table>
		
		<style>
.foot_header {position:relative; font-family:Verdana, Geneva, sans-serif; font-size:11px; font-weight:bold; color:#FFF;}
.foot_links {position:relative; font-family:Verdana, Geneva, sans-serif; font-size:10px; color:#FFF; line-height:16px; text-decoration:none;}
.foot_links:hover {position:relative; font-family:Verdana, Geneva, sans-serif; font-size:10px; color:#FFF; line-height:16px; text-decoration:underline;}
.foot_copyright {position:relative; font-family:Verdana, Geneva, sans-serif; font-size:9px; color:#FFF; line-height:16px; text-decoration:none;}
.foot_copyright:hover {position:relative; font-family:Verdana, Geneva, sans-serif; font-size:9px; color:#FFF; line-height:16px; text-decoration:underline;}
</style>

<!-- Main Footer-->

<!--
<script type="text/javascript" src="https://www.ncix.com/js/jquery.min.js"></script>
<script type="text/javascript" src="https://www.ncix.com/js/jquery-ui-1.8.2.custom.min.js"></script>
<script type="text/javascript" src="https://www.ncix.com/js/jquery.cycle.all.min.js"></script>
<script type="text/javascript" src="https://www.ncix.com/js/ncix.js?v=20160805"></script>
-->
<!--
<link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Roboto:400,300,700">
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800,300" rel='stylesheet' type='text/css'>
<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400" rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Roboto:400,300,500,700,900' rel='stylesheet' type='text/css'>
<link rel="canonical" href="https://www.ncix.com/" />
<link rel="stylesheet" href="https://www.ncix.com/css/ncix.min.20170727.css" type="text/css">
-->
<style>
#popularcat-brands {
position: relative;
text-align:center;
width:100%;
height:51px;
overflow:hidden;
border-width:0px;
border-color:#666666;
border-style:solid;
}
#popbox-brands {
position: relative;
width:auto;
overflow:hidden;
float:left;
min-width:110px;
margin: 0px auto;
}
#popbox-brands {
position: relative;
width:auto;
overflow:hidden;
float:left;
min-width:130px;
margin: 0px auto;
}
.populartitle-brands {
font-family:'Open Sans', Arial, Helvetica, sans-serif;
font-size:20px;
font-weight:bold;
color:#000000;
text-decoration:none;
}
.populartext-brands {font-family: Verdana, Geneva, sans-serif; font-size:11px; color:#0054a6; text-decoration:none; text-align:center;}
.populartext-brands:hover {font-family: Verdana, Geneva, sans-serif; font-size:11px; color:#0054a6; text-decoration:underline;}
.seeallproducts-brands {font-family: Verdana, Geneva, sans-serif; font-size:11px; color:#0054a6;}
.clearout {
height:1px;
clear:both;
}
.subpromoHomeBorder {
border-top: #C39 2px;
}
.footer-spacing {line-height:37px; }
a.foot_links-Two {text-decoration:none;}
a.foot_links-Two:link,a.foot_links-Two:hover{
position:relative;
font-family:'Open Sans', Roboto,Verdana,Geneva,sans-serif;
font-size:14px;
font-weight:600;
}
a.foot_links-Two{color:#F1f1f1;}
a.foot_links-Two:hover{
text-decoration:underline;
color:#FFF;
}
.foot_links-Header {
position:relative;
font-family:'Open Sans', Roboto,Verdana,Geneva,sans-serif;
font-size:16px;
font-weight:600;
color:#e5e5e5;
padding-bottom:1px;
}
.footer-horizontal-line {
margin-top:13px;
margin-bottom:13px;
width:90%;
size:1;
border-color:#838383;
}
.footer-background {
background-color:#666666;
}
.footer-background-lighter {
background-color: #a6a6a6;
}
.footer-background-darker {
background-color: #353535;
}
.footer-background-middark {
background-color:#4f4f4f;
}
.footer-vertical-line div {
border: 2px solid #f00;
margin: -2px;
}
.vertical_line{ width:1px;background:#000; height:100%; display: inline-block}
#Subpromo-Mid-Border {
border-top:1px #e8e8e8 solid;
padding-top: 10px;
}
#Subpromo-Product-Savings-text {
font-weight:bold;
font-family:Verdana, sans-serif;
font-size:13px;
color:#cc3300;
}
#Subpromo-Product-Savings-text2 {
font-weight:400;
font-family:Verdana, sans-serif;
font-size:12px;
color: #333;
}
#Subpromo-Product-Price-text {
font-weight:400;
font-family:Verdana, sans-serif;
font-size:11px;
}
@-moz-document url-prefix() {
.divLineTriangle {
margin-top:2px;
}
}
a.SKU-title-link:link{
color:#313131;
}
a.SKU-title-link:visited{
color:#313131;
}
a.SKU-title-link:hover ~ SKU-title-link-arrow{
color: #005cb6;
}
a.SKU-title-link:active{
color:#f00;
}
a.SKU-title-link-arrow:link{
color:#e8e8e8;
}
a.SKU-title-link-arrow:visited{
color:#e8e8e8;
}
a.SKU-title-link-arrow:hover ~ a:SKU-title-link{
color: #005cb6;
}
a.SKU-title-link-arrow:active{
color:#f00;
}
.overlay {
position: absolute;
top: 0;
bottom: 0;
left: 0;
right: 0;
height: 100%;
width: 100%;
opacity: 0;
transition: .5s ease;
background-color: #008CBA;
}
.container:hover .overlay {
opacity: 1;
color:#090
}
</style>
<div class="footer-background-middark">
<table width="90%" cellpadding="7" cellspacing="0" border="0" class="footer-spacing" align="center" >
<tr>
<td >
<!-- Start -->
<table >
<tr><td >
<table id="social_footer" height="50" border="0" cellpadding="0" cellspacing="0" >
<tr>
<td class="payment-type-padding">
<div class="foot_links-Header">Shop with Confidence</div>
</td></tr></table>
<table id="social_footer" height="50" border="0" cellpadding="0" cellspacing="0" >
<tr>
<td class="payment-type-padding">
<!-- START SCANALERT CODE -->
<a href="https://www.scanalert.com/RatingVerify?ref=www.ncix.com" target="_blank" rel="nofollow"><img alt="HACKER SAFE certified sites prevent over 99.9% of hacker crime." src="https://images.scanalert.com/meter/www.ncix.com/13.gif" border="0" style="padding-top:4px;"></a>
<!-- END SCANALERT CODE -->
</td>
<td class="payment-type-padding">
<div style="text-align: center; padding-bottom:7px;">
<a href="https://www.bbb.org/mbc/business-reviews/computer-dealers/netlink-computers-in-richmond-bc-136226" target="_blank" rel="nofollow"><img src="https://dhsj95t7aazhx.cloudfront.net/Footer/BBB-Accredited-Business2.png" alt="Click to verify BBB accreditation and to see a BBB report." width="107" height="41" border="0" title="Click to verify BBB accreditation and to see a BBB report." oncontextmenu="alert('Use without permission is prohibited. The BBB Accreditation seal is a trademark of the Council of Better Business Bureaus, Inc.'); return false;"></a></div>
</td>
</tr>
</table>
</td>
<td align="center" >
<a href="https://www.resellerratings.com/store/NCIX"><img src="https://dhsj95t7aazhx.cloudfront.net/Footer/Reseller-Ratings-elite-badge-transparent.png" alt="Reseller Ratings Elite Member" border="0" style="margin-top:9px; padding-left:18px;" /></a>
</td></tr></table>
</td>
<td height="100%" >
<table>
<tr><td height="15px"></td></tr>
<tr>
<!--
<td style="border-right:1px #838383 inset; margin-top:5px; " valign="bottom" height="90px">&nbsp;
</td>
-->
<td background="https://dhsj95t7aazhx.cloudfront.net/Footer/Vertical-footer-line-grey.png" style="padding-right:20px; background-repeat:repeat-y" height="95px">
</td>
</tr>
</table>
</td>
<td >
<table id="social_footer" height="50" border="0" cellpadding="0" cellspacing="0" >
<tr>
<td class="payment-type-padding">
<div class="foot_links-Header">We're mobile!</div>
</td></tr></table>
<table id="social_footer" height="50" border="0" cellpadding="0" cellspacing="0" >
<tr>
<td class="payment-type-padding" >
<a href="https://bit.ly/1T8VV94"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/footer_social/footer_social_01.png" width="128" height="50" border="0" alt="NCIX Android App - Android App on Google Play"></a></td>
<td class="payment-type-padding">
<a href="https://tinyurl.com/a49ngav"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/footer_social/footer_social_02.png" width="129" height="50" border="0" alt="NCIX iOS App - Available on the App Store"></a></td>
<td class="payment-type-padding">
<a href="https://bit.ly/1guO0Pn"><img src="https://dhsj95t7aazhx.cloudfront.net/bnr/footer_social/socialmedia_win8.png" height="50" border="0" alt="NCIX Windows Mobile App"></a></td>
</tr>
</table>
</td></tr>
</table>
<table width="100%" cellpadding="0" cellspacing="0" >
<tr>
<td align="center" >
<div style="height:10px;"></div>
<hr class="footer-horizontal-line" width="90%" align="center" NOSHADE size="1" color="#330066" >
</td></tr></table>
<!-- Main Footer-->
<table width="100%" cellpadding="7" cellspacing="0" class="footer-spacing" >
<tr><td height="28px"></td></tr>
<tr >
<td width="5%"></td>
<td valign="top" width="19%" >
<div class="foot_links-Header">Your Order</div>
<a href="https://secure1.ncix.com/customersupport/" target="_self" class="foot_links-Two">Order Status</a><br>
<a href="https://secure1.ncix.com/customersupport/?mode=customersupport&tab=3&action=new" target="_self" class="foot_links-Two">RMAs (Merchandise returns)</a><br>
<a href="https://www.ncix.com/article/customercare.htm" target="_self" class="foot_links-Two">F.A.Q.</a><br>
<a href="https://secure.ncix.com/message/" target="_self" class="foot_links-Two">Send Us a Message</a><br>
</td>
<td background="https://dhsj95t7aazhx.cloudfront.net/Footer/Vertical-footer-line-grey.png" style="padding-right:20px; background-repeat:repeat-y" >
</td>
<td valign="top" width="19%" style="border-left:#063 1px;" height="100%">
<div class="foot_links-Header">Company Info</div>
<a href="https://www.ncix.com/contact/" target="_self" class="foot_links-Two">Contact Us </a><br>
<!-- <a href="https://www.ncix.com/article/careers.htm" target="_self" class="foot_links-Two">Careers</a><br>-->
<a href="https://technews.ncix.com/" target="_self" class="foot_links-Two">Blog</a><br>
<a href="https://www.ncix.com/article/customercare.htm#terms" target="_self" class="foot_links-Two">Terms & Conditions</a><br>
<a href="https://www.ncix.com/article/privacy.htm" target="_self" class="foot_links-Two">Privacy Policy</a><br>
<a href="https://www.bbb.org/mbc/business-reviews/computer-dealers/netlink-computers-in-richmond-bc-136226" target="_self" class="foot_links-Two">BBB Accredited Business Profile</a><br>
<a href="https://www.ncix.com/article/NCIX-Branding-and-Logos.htm" target="_self" class="foot_links-Two">Branding & Logos</a><br>
</td>
<td valign="top" width="19%">
<div class="foot_links-Header">Memberships</div>
<a href="https://www.ncix.com/article/ncix-rewards.htm" target="_self" class="foot_links-Two">NCIX Rewards</a><br>
<a href="https://www.ncix.com/article/premier_partner.htm" target="_self" class="foot_links-Two">Premier Partner Reseller Program</a> <br>
<a href="https://www.ncix.com/article/vip.htm" target="_self" class="foot_links-Two">VIP Memberships</a><br>
<a href="https://www.ncix.com/article/ncix_advantage.htm" target="_self" class="foot_links-Two">Advantage Membership</a><br>
<a href="https://ncix.postaffiliatepro.com/affiliates/signup.php" target="_self" class="foot_links-Two">NCIX Affiliate Program</a> <br />
<!--<a href="https://www.ncix.com/supershippingsaverclub" target="_self" class="foot_links-Two">Super Shipping Saver Club</a><br>-->
</td>
<td valign="top" width="19%">
<div class="foot_links-Header">Services</div>
<a href="https://www.ncix.com/article/expresscoverage.htm" target="_self" class="foot_links-Two">Express Coverage</a><br>
<a href="https://www.ncix.com/article/expressrma.htm" target="_self" class="foot_links-Two">Express RMA</a><br>
<a href="https://www.ncix.com/article/warranty.htm" target="_self" class="foot_links-Two">Express Exchange & Care Coverage</a><br>
<a href="https://www.ncix.com/article/ncix-giftcards.htm" target="_self" class="foot_links-Two">Gift Cards & Balance Checker</a><br>
<a href="https://www.ncix.com/article/same-day-delivery.htm" target="_self" class="foot_links-Two">Same-Day Delivery </a><br>
<a href="https://www.ncix.com/article/desjardins.htm" target="_self" class="foot_links-Two">Retail Financing</a><br>
</td>
<td valign="top" width="19%">
<div class="foot_links-Header">Hot Links</div>
<a href="https://www.ncix.com/newsletters/" target="_self" class="foot_links-Two">NCIX Newsletters</a><br>
<a href="https://secure1.ncix.com/prize/" target="_self" class="foot_links-Two">Prize Picker</a><br>
<a href="https://www.ncix.com/products/?mode=rebates" target="_self" class="foot_links-Two">Rebate Center</a><br>
<!-- <a href="https://www.mirhelp.com/" target="_self" class="foot_links-Two">Rebate Archive</a><br> -->
<a href="https://forums.ncix.com/" target="_self" class="foot_links-Two">NCIX Forums</a><br>
<a href="https://www.ncix.com/article/folding_team_center.htm" target="_self" class="foot_links-Two">Folding @ Home Team</a><br>
<a href="https://www.thebannervault.com/" target="_self" class="foot_links-Two">The Banner Vault</a><br>
</td>
<td width="5%" > </td>
</tr>
</table>
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr >
<td>
<style>
.payment-type-padding {
padding-left:25px;
padding-right:25px;
}
</style>
<center>
<div style="height:10px;"></div>
<hr class="footer-horizontal-line" NOSHADE size="1">
<table id="social_footer" height="50" border="0" cellpadding="0" cellspacing="10" >
<tr>
<td class="payment-type-padding">
<img src="https://dhsj95t7aazhx.cloudfront.net/Footer/Visa-Checkout.png" width="154" height="34" border="0" alt=""></td>
<td class="payment-type-padding">
<a href="https://masterpass.com/en-ca/"><img src="https://dhsj95t7aazhx.cloudfront.net/Footer/Masterpass-checkout.png" width="147" height="34" border="0" alt="NCIX iOS App - Available on the App Store"></a></td>
<td class="payment-type-padding"><img src="https://dhsj95t7aazhx.cloudfront.net/Footer/American-Express.png" height="66" border="0" alt="American Express"></td>
<td valign="middle" class="payment-type-padding">
<img src="https://dhsj95t7aazhx.cloudfront.net/Footer/Paypal-checkout.png" width="170" height="32" border="0" alt="Paypal">
</td>
<td class="payment-type-padding">
<img src="https://dhsj95t7aazhx.cloudfront.net/Footer/Interac-Online.png" width="107" height="54" border="0"alt="NCIX YouTube">
</td>
</tr>
</table>
<hr class="footer-horizontal-line" NOSHADE size="1">
<!--
<div itemscope itemtype="https://schema.org/LocalBusiness" class="foot_links-Two">
<div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
<span itemprop="name">NCIX.com</span>,
<span itemprop="streetAddress" >13720 Mayfield Place</span>
<span itemprop="addressLocality">Richmond</span>,
<span itemprop="addressRegion">British Columbia</span>
<span itemprop="addressCountry">Canada</span>
<span itemprop="postalCode">V6V 2E4</span>.
Phone: <span itemprop="telephone">604-288-8080</span>
</div>
</div>-->
</center>
</td>
</tr>
<tr><td align="center">
<style>
.WeChattooltip {
position: relative;
display: inline-block;
cursor:pointer;
}
.WeChattooltip .WeChattooltiptext {
visibility: hidden;
width: 270px;
background-color: #e2e2e2;
color: #000;
text-align: left;
border-radius: 4px;
padding: 8px 10px;
position: absolute;
z-index: 1;
bottom: 125%;
left: 50%;
margin-left: -134px;
opacity: 0;
transition: opacity 1s;
font-weight:normal;
}
.WeChattooltip:hover .WeChattooltiptext {
visibility: visible;
opacity: 1;
}
</style>
<center>
<br />
<table id="social_footer" height="50" border="0" cellpadding="0" cellspacing="0" >
<tr>
<!--
<td>
<img src="https://dhsj95t7aazhx.cloudfront.net/bnr/footer_social/footer_social_03.png" width="19" height="50" border="0" alt=""></td> -->
<td style="padding-right:16px;">
<div class="foot_links-Header">Stay Connected </div>
</td>
<td>
<span itemscope itemtype="https://schema.org/Organization">
<link itemprop="url" href="https://www.ncix.com">
<a itemprop="sameAs" href="https://www.facebook.com/NCIXdotCOM"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-facebook.png" width="46" height="50" border="0"alt="NCIX Facebook"></a>
<a itemprop="sameAs" href="https://www.youtube.com/user/NCIXcom"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-youtube.png" width="48" height="50" border="0"alt="NCIX YouTube"></a>
<a itemprop="sameAs" href="https://www.twitter.com/NCIXdotCOM"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-twitter.png" width="48" height="50" border="0"alt="NCIX Twitter"></a>
<a itemprop="sameAs" href="https://plus.google.com/101746540581038237777"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-googleplus.png" alt="Google +1" width="48" height="50" border="0"></a>
<a itemprop="sameAs" href="https://www.instagram.com/ncixdotcom"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-instagram.png" width="48" height="50" border="0" alt="NCIX Instagram"></a>
<a itemprop="sameAs" href="https://www.pinterest.com/source/ncix.com/"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-pinterest.png" width="48" height="50" border="0" alt="NCIX Pinterest"></a>
</span>
<a href="https://forums.ncix.com/"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-forums.png" width="48" height="50" border="0" alt="NCIX Forum"></a>
<span class="WeChattooltip"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/footer_social-WeChat.png" width="48" height="50" border="0" alt="NCIX WeChat">
<span class="WeChattooltiptext"><img src="https://dhsj95t7aazhx.cloudfront.net/footer-social/WeChat-QRcode-250.gif" border="0"></span>
</span>
</span>
</td>
</tr>
</table>
<!--
<div itemscope itemtype="https://schema.org/LocalBusiness" class="foot_links">
<div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress">
<span itemprop="name">NCIX.com</span>,
<span itemprop="streetAddress" >13720 Mayfield Place</span>
<span itemprop="addressLocality">Richmond</span>,
<span itemprop="addressRegion">British Columbia</span>
<span itemprop="addressCountry">Canada</span>
<span itemprop="postalCode">V6V 2E4</span>.
Phone: <span itemprop="telephone">604-288-8080</span>
</div>
</div>-->
</center>
</td></tr>
<!--
<tr >
<td align="center">
<style>
.footerlink {font-family:Verdana, Geneva, sans-serif; font-size:11px; line-height:18px; color:#fff; text-decoration:none;}
.footerlink:hover {font-family:Verdana, Geneva, sans-serif; font-size:11px; line-height:18px; color:#fff; text-decoration:none;}
</style>
<span class="footerlink">International Sites:
<a href="https://www.ncixus.com/"> <img src="https://d1sfu4378rr01a.cloudfront.net/_img/icon_us.gif" border="0"></a>
<a href="https://www.ncix.com/" class="footerlink"> <img src="https://d1sfu4378rr01a.cloudfront.net/_img/icon_cdn.gif" border="0">&nbsp;Canada</a>
</span>
</td>
</tr>
-->
</table>
<br />
</div>


<table width="100%" cellpadding="0" cellspacing="0" border="0">
	<tr bgcolor="#4f4f4f">
		<td align="center">
			<style>
			.footerlink {font-family:Verdana, Geneva, sans-serif; font-size:11px; line-height:18px; color:#fff; text-decoration:none;}
			.footerlink:hover {font-family:Verdana, Geneva, sans-serif; font-size:11px; line-height:18px; color:#fff; text-decoration:none;}
			</style>
			<span class="footerlink">International Sites: 
			<a href="https://www.ncixus.com/"> <img src="https://d1sfu4378rr01a.cloudfront.net/_img/icon_us.gif" border="0"></a> 
			<a href="https://www.ncix.com/" class="footerlink"> <img src="https://d1sfu4378rr01a.cloudfront.net/_img/icon_cdn.gif" border="0">&nbsp;Canada</a>
			</span>
		</td>
		</tr>
		<tr bgcolor="#4f4f4f">
			<td>
				
				
				<!-- Extra footer space here -->
				
			</td>
		</tr>
		
		<tr bgcolor="#4f4f4f">
			<td align="center">
					
						<font  style="font-family:Verdana, Geneva, sans-serif; font-size:9px; color:#FFF;"><h1>Buy DDR3 SODIMM Memory</h1>
<p>If you are looking to <b>buy DDR3 SODIMM</b>, DDR3 SDRAM memory in Canada then shop at NCIX for cheap computer memory to buy laptop memory or desktop memory or if when you want to upgrade your computer. </p>
<p> If you want to buy DDR3 SODIMM which is a small outline dual in-line memory module, is a type of computer memory built using integrated circuits than NCIX has the best and cheapest prices to buy computer memory in Canada.</p>
<p>Buy DDR3 SODIMM at NCIX to <b>buy computer memory</b> in Canada like laptop memory, server memory and desktop memory at the best discount computer for memory.</p></font><br />
					
					<span style="position:relative; font-family:Verdana, Geneva, sans-serif; font-size:9px; color:#FFF; line-height:16px; text-decoration:none;">Copyright&copy; 2018 NCIX.com/Netlink Computer Inc. All rights reserved. 
					/ Server ID:
					
						
						21
						
					
					&nbsp;2031 ms <br />
					Page last updated: 05/27/2018 04:31:50</span>
			</td>
		</tr>
	</table>
<script type="text/javascript">
	doReferer();
	CheckAffiliate();
	displayssslogo();
</script>



	
	

	<script language="javascript">
	$(function(){
	
		$("ul.dropdown li").hover(function(){
		
			$(this).addClass("hover");
			$('ul:first',this).css('visibility', 'visible');
		
		}, function(){
		
			$(this).removeClass("hover");
			$('ul:first',this).css('visibility', 'hidden');
		
		});
	
	});
</script>


		<script type="text/javascript"><!--
		document.write(unescape("%3Cscript id='pap_x2s6df8d' src='" + (("https:" == document.location.protocol) ? "https://" : "http://") +
		"ncix.postaffiliatepro.com/scripts/trackjs.js' type='text/javascript'%3E%3C/script%3E"));//-->
		</script>
		<script type="text/javascript"><!--
		PostAffTracker.setAccountId('default1');
		try {
		PostAffTracker.track();
		} catch (err) { }
		//-->
		</script>

<script src="/js/jquery.main.js"></script>
</td>
</tr>
</table>



	<!-- Start Alexa Certify Javascript -->
	<script type="text/javascript">
	_atrk_opts = { atrk_acct:"hNTWi1a4ZP00wk", domain:"ncix.com",dynamic: true};
	(function() { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://d31qbv1cthcecs.cloudfront.net/atrk.js"; var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as, s); })();
	</script>
	<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=hNTWi1a4ZP00wk" style="display:none" height="1" width="1" alt="" /></noscript>
	<!-- End Alexa Certify Javascript -->
	


	
	<noscript>
	<img height="1" width="1" style="display:none;" alt="" src="https://analytics.twitter.com/i/adsct?txn_id=l5bms&p_id=Twitter" />
	<img height="1" width="1" style="display:none;" alt="" src="//t.co/i/adsct?txn_id=l5bms&p_id=Twitter" /></noscript>
	<!-- BEGIN: Google Certified Shops -->
	
	<script type="text/javascript">
	  var gts = gts || [];
	
	
	  gts.push(["id", "500541"]);
	  gts.push(["badge_position", "BOTTOM_RIGHT"]);
	  gts.push(["locale", "en_US"]);
	  gts.push(["google_base_subaccount_id", "100323107"]);
	  gts.push(["google_base_country", "EN"]);
	  gts.push(["google_base_language", "en"]);
	
	  (function() {
		var gts = document.createElement("script");
		gts.type = "text/javascript";
		gts.async = true;
		gts.src = "https://www.googlecommerce.com/trustedstores/api/js";
		var s = document.getElementsByTagName("script")[0];
		s.parentNode.insertBefore(gts, s);
	  })();
	</script>
	<!-- END: Google Certified Shops -->




<script type="text/javascript">
/* <![CDATA[ */
    var ecomm_prodid= '';
    var ecomm_pagetype= '';
    var ecomm_totalvalue= 0;
    var pathnameVal=window.location.pathname;
    
    if(pathnameVal.indexOf('/cart/')==0)/* for cart page */
    {
      
      var productId=new Array();

      jQuery('.linecarttop>font.listing:not(:contains("$"))').each(function(){
        var prodId=jQuery(this).text();
        productId.push(prodId);
      });
     
      var price=0;
      try{
      price=parseFloat(jQuery('#carttotal').text().replace(/[^0-9.]/g,''));
    }catch(e)
    {}
      ecomm_prodid= productId; 
      ecomm_pagetype= 'cart';
      ecomm_totalvalue=price;
    }else
    if(pathnameVal.indexOf('/detail/')==0) /* for product page */
    {
      var productId=jQuery('[name="frmaddtocart"]').attr('action').split('additem=')[1].split('&')[0];
      
      var price=0;
      try{
      price=jQuery('[itemprop="price"]:first').text().replace(/[^0-9.]/g,'');
    }catch(e)
    {}
      ecomm_prodid= productId; 
      ecomm_pagetype= 'product';
      ecomm_totalvalue=price;
    }else
    if(pathnameVal=='/')/* for home page */
    {
      ecomm_pagetype= 'home';
    }else
    if(pathnameVal.indexOf('/category/')==0 || pathnameVal.indexOf('/vendor/')==0)/* for category page */
    {
      ecomm_pagetype= 'category';
    }else
    {
      ecomm_pagetype= 'other'; /* for other page */
    }
    var google_tag_params = {
      ecomm_prodid: ecomm_prodid, 
      ecomm_pagetype: ecomm_pagetype,
      ecomm_totalvalue: parseFloat(ecomm_totalvalue)
    };
    
  /* ]]> */
</script>

	
		<script type="text/javascript"> 
		/* <![CDATA[ */ 
		var google_conversion_id = 1071851262; 
		var google_custom_params = window.google_tag_params; 
		var google_remarketing_only = true; 
		/* ]]> */ 
		</script> 
		<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js"> 
		</script> 
		<noscript> 
		<div style="display:inline;"> 
		<img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/1071851262/?value=0&amp;guid=ON&amp;script=0"/> 
		</div> 
		</noscript>
	



</body>
</html>

	





		
		 
    """
    # subCat = requests.get(url, timeout=5)
    subCatContent = BeautifulSoup(pageContent, 'html.parser')
    listing = subCatContent.select("td > span.listing a")
    for l in listing:
        image = l.parent.parent.parent.find("img", attrs={"title": l.string})
        print(image['src'])
        break

scrapNcixListing("https://www.ncix.com/category/ddr3-memory-d0-1303.htm")

