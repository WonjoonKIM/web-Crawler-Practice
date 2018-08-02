from bs4 import BeautifulSoup as B

html="""<<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">

<html>
  <head>
    <meta charset='utf=8'>
    <meta http-equiv="Content-Type" content="text/html; charset=EUC-KR"/>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    <title>EDWARD 포털 통합로그인</title>
    <link rel="stylesheet" type="text/css" href="../../resources/css/ext-all.css" />
    <link rel="stylesheet" type="text/css" href="../../resources/css/xtheme-blue.css" />
    <link rel="stylesheet" type="text/css" href="../../css/style.css"/>
    <link rel="stylesheet" type="text/css" href="../../css/login.css"/>
    <script language="javascript" type="text/javascript" src="../../js/ext-base.js"></script>
    <script language="javascript" type="text/javascript" src="../../js/ext-all.js"></script>
    <script language="javascript" type="text/javascript" src="/XecureObject/xecureweb.js"></script>
    <script language="javascript" type="text/javascript" src="/XecureObject/xecureweb_custom.js"></script>
    <script language="javascript" type="text/javascript" src="../../js/common.js"></script>
    <script language="javascript" type="text/javascript">
    //<![CDATA[
    var s = '';
s += '-----BEGIN CERTIFICATE-----\n';
s += 'MIIDsjCCApqgAwIBAgICCSwwDQYJKoZIhvcNAQEFBQAwgZIxCzAJBgNVBAYTAktS\n';
s += 'MR4wHAYDVQQKExVTb2Z0Zm9ydW0gQ29ycG9yYXRpb24xHjAcBgNVBAsTFVNlY3Vy\n';
s += 'aXR5IFJORCBEaXZpc2lvbjEcMBoGA1UEAxMTU29mdGZvcnVtIFB1YmxpYyBDQTEl\n';
s += 'MCMGCSqGSIb3DQEJARYWY2FtYXN0ZXJAc29mdGZvcnVtLmNvbTAeFw0xNDA4MDcw\n';
s += 'ODQ1NTBaFw0xNTA4MTQwODQ1NTBaMF4xCzAJBgNVBAYTAktSMQwwCgYDVQQKDANL\n';
s += 'TVUxDDAKBgNVBAsMA0lUUzESMBAGA1UEAwwJa211LmFjLmtyMR8wHQYJKoZIhvcN\n';
s += 'AQkBFhBtYXN0ZXJAa211LmFjLmtyMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKB\n';
s += 'gQCU0Lm1uT0a50lecBG/f1HYPXDXy+GWnzlooFyms2bKoIExyqSGSZ9lE41G6sVY\n';
s += 'aer6yKGdv5Ixc6pzgeV+jczav4EQavREDtYmTG89hrW9gkmxcmNbbHAfu/EJTD/8\n';
s += 'TINzZq73U1ufkuCKEPjOkO6Y3XOnVUxfbeZ7gGue7lm29QIDAQABo4HIMIHFMB8G\n';
s += 'A1UdIwQYMBaAFC5JqyeK6Mivl3U33ot0uyQODSdfMB0GA1UdDgQWBBSGjcI92fur\n';
s += 'qN52iyT0mjkD1fnIvjALBgNVHQ8EBAMCBLAwDAYDVR0TAQH/BAIwADBoBgNVHR8E\n';
s += 'YTBfMF2gW6BZhldsZGFwOi8vbGRhcC5zb2Z0Zm9ydW0uY28ua3I6Mzg5L2NuPXNl\n';
s += 'LG89c29mdGZvcnVtLGM9a3I/Y2VydGlmaWNhdGVSZXZvY2F0aW9ubGlzdDtiaW5h\n';
s += 'cnkwDQYJKoZIhvcNAQEFBQADggEBAAlPQ3E5kj0YGk0JleSB9tcAH/Y6T6eb2Oto\n';
s += 'd9be1g5qYA054a4oRDMJGSEMYV5v4urYFjKTuFIX9GF1wJwvrmGeDGx1juNab+u+\n';
s += 'wUNYSrl+ce+D5YfIUyxYlnd0nR6RKBBDXFAZQ40A+89DROrimUkj7oI+R9+oCTBq\n';
s += 'ZzNc7Y5WP4/4aM6WOAi2gZoBeayiDRRue3C6hrZt919Zw/oqcjzA7egs3rB7agrt\n';
s += 'im/jNWF8l1huBe8LNBUgycKnRIY0XBXtMDY+Ez299LSci9JgMlrhy6aCsC7M50o4\n';
s += 'ztfss+TH5yqBUdSLrd8Du6aH0UQqi9otxj1oA2dfidMc0O9Owck=\n';
s += '-----END CERTIFICATE-----\n';
s += '';

    //]]>
    </script>
    <script language="javascript" type="text/javascript" src="../../js/login_form_common.js"></script>
    <script type="text/javascript">
    function chkPassword() {
        var openLocation = "http://edward.kmu.ac.kr/nx/index_external.html?bWVudUlkPU0zMjEwNzY=";
        mywin = window.open(openLocation,"edward_pwd","width=505, height=390, top=100, left=100");
        mywin.focus();
    }
    
    function findClassNum() {
        var openLocation = "http://edward.kmu.ac.kr/nx/index_external.html?bWVudUlkPU0zMjEwNzc=";
        mywin2 = window.open(openLocation,"edward_hakbun","width=418, height=375, top=100, left=100");
        mywin2.focus();
    }
    
    function localeChange() {
    	document.idLoginForm.locale.value = document.certLoginForm.locale.value; 
    }
    
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-17055096-6']);
      _gaq.push(['_trackPageview']);
    
      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
    
    </script>
  </head>
  <body style="background:url(../../img/ext/edward/login_bg.png) repeat-x;" onload="jf_onload();">
<!-- 전체감싸기 -->
<div id="login_wrap">
  
    <div id="skipnavi"> <a href="#login_navi">로그인 바로가기</a> <a href="#board_navi">작업공지 바로가기</a> </div>
    
   <div id="login_wrap_center">
   
   <div>
   <img src="../../img/ext/edward/login_logo.png" alt="계명대학교 EDWARD포털">
   </div> 
  
   <!-- 중간학교 문구,이미지 S-->
   <ul class="login_subimg_area">
   <li class="left_pi1"><img src="../../img/ext/edward/login_top_text01.png" alt="계명대학교 통합로그인센터에 오신것을 환영 합니다."></li>
   <li class="right_pi1"><img src="../../img/ext/edward/login_top_pi01.jpg" alt="학교건물이미지"></li>
   </ul>
   <!-- 중간학교 문구,이미지 E-->
   
   
    <!-- 로그인,작업공지 S-->
   <div class="login_area">
   
  
   <!-- 로그인 S-->
   <div id="login_navi">
     <div class="login_s" style="height:300px; display:inline-block;">
        <fieldset>
              <legend>로그인</legend>
              <!-- 로그인 박스 -->
      <form name="idLoginForm" method="POST" action="login_process.do" onsubmit="return jf_idlogin(this);">
      <select style="display:none" name="locale" id="locale"  class="se_int" title="선택" style="width:150px;">
                                     <option value="ko" selected>한글(Korea)</option>
                                     <option value="en" >영어(English)</option>
             </select>
      <input type="hidden" name="Return_Url" value="https://edward.kmu.ac.kr/com/SsoCtr/sso_login.do?redirectUrl=https://portal.kmu.ac.kr/proc/Login.do" />
      <input type="hidden" name="loginType" value="ID" />
        <dl>
        <dt class="log_tit">로그인</dt>
          <dd  style="display:inline-block;">
           <ul class="login_input_area">
                  <li class="input_row01">
                    <label for="usr_id" id="label_id_area00" class="blind"  >아이디</label>
                    <input type="text" name="loginName" autocomplete="off" onkeyup="jf_nextfield(event, document.idLoginForm.password);" tabindex="1" class="int" id="usr_id" accesskey="L" placeholder="아이디" class="int" maxlength="20"/ >
                  </li>
                   <li class="input_row02">
                    <label for="usr_pw" id="label_id_area11" class="blind"  >비밀번호</label>
                    <input type="password" id="usr_pw" name="password" autocomplete="off" onkeyup="jf_enter_submit(event, document.idLoginForm);" tabindex="2"  accesskey="L" placeholder="비밀번호" class="int" maxlength="20" enc="Off"/ >
                  </li>
                </ul>
                <ul class="login_bu_area" >
                  <li style="height:50px"><a href="#" onclick="return document.idLoginForm.onsubmit();" tabindex="3"><img src="../../img/ext/edward/login_bu2.png" alt="로그인"/></a></li>
                </ul>
         </dd> 
        </dl>
      </form>
     </fieldset>
        
     <div class="login_area_line"> </div>
             
     <fieldset>
              <legend>공인인증서 로그인</legend>
              <!-- 로그인 박스 -->
       <form name="certLoginForm" action="login_process.do" method="POST" onsubmit="return jf_certlogin(this);">
       <input type="hidden" name="Return_Url" value="https://edward.kmu.ac.kr/com/SsoCtr/sso_login.do?redirectUrl=https://portal.kmu.ac.kr/proc/Login.do" />
       <input type="hidden" name="plain" />
       <input type="hidden" name="signedMsg" />
       <input type="hidden" name="vidMsg" />
       <input type="hidden" name="loginType" value="CERT" />
        <dl>
        <dt></dt>
          <dd>
           <ul class="login_input_area">
                <li class="input_row">
                    <label for="usr_id2" id="label_id_area" class="blind"  >인증서 로그인</label>
                    <input type="text" id="usr_id2" name="loginName" tabindex="4" accesskey="L" placeholder="아이디" class="int" maxlength="20"/ >
                  </li>
                </ul>
                <ul class="login_bu_area">
                  <li><a href="#" onclick="return document.certLoginForm.onsubmit();" tabindex="5"><img src="../../img/ext/edward/login_bu1.png" alt="공인인증서로그인"/></a></li>
                </ul>
         </dd> 
         <dd>
           <ul class="login_area_se" style="float: left;">
             <li style="float: left;">
             <select name="locale" id="locale"  class="se_int" onchange="localeChange();" title="선택" style="width:150px;">
                                     <option value="ko" selected>한글(Korean)</option>
                                     <option value="en" >영어(English)</option>
             </select>
             </li>
           </ul>
        </dd>
        </dl>
      </form>
     </fieldset>
     </div>
     </div>
    <!-- 로그인 E-->
    
    <!-- 작업공지 S-->
<div id="board_navi" style="display: inline-block; width: 50%;">
     <iframe src="https://portal.kmu.ac.kr/eXPortal/pages/login/kmuNoticeList.jsp" style="border: 0px; width: 100%; height: 260px;" scrolling="no"></iframe>
 </div>
    <!-- 작업공지 E-->
   

   
   </div>
   <!-- 로그인,작업공지 E-->
   
   <!-- 알아두어야할 사항 S-->
   <div class="notice_info">
   <ul>
   알아두실 사항
   
   <li class="notice_list01">서비스 이용을 끝낸 후에는 개인정보보호를 위하여 꼭 로그아웃을 해 주시기 바랍니다.</li>
   <li class="notice_list02">학생 : 아이디는 학번이며, 최초비밀번호는 주민등록번호 뒷자리(7자) 입니다.</li>
   <li class="notice_list02" style="
    color: red;
">교수/직원 : 아이디는 신인사번호, 비밀번호는 웹정보시스템과 동일</li><li class="notice_list02" style="
    background: none;
    padding-left: 82px;
    color: red;
    ">※신인사번호: 5자리 인사번호 체계에서 6자리 인사번호 체계로 변경</li>
    <li class="notice_list02" style="
    background: none;
    padding-left: 96px;
    color: red;">현재 인사번호의 두 번째 자리에 '0' 을 삽입 -> 1XXXX (기존) 10XXXX(변경)</li>
   <li class="notice_list02" style="
    background: none;
    color: red;
    ">[EDWARD Systems require your NEW ID]</li>
    <li class="notice_list02" style="
    background: none;
    color: red;
    ">5 digit ID number to 6 digit [Add '0, zero' after 1 or 2: 1XXXX -> 10XXXX, e.g.) 11052 -> 101052]
    </li>
    <li class="notice_list03">
    <a href="http://www.kmu.ac.kr/page.jsp?mnu_uid=2734" onclick="window.open(this.href,'Policy', 'scrollbars=yes, width=1000px,height=720px');return false;" 
    style="text-decoration:none" target="_blank">
        <img src="../../img/policy.png" alt="개인정보처리방침"/>
     </a> 
     </li>
    
    <li class="pw_find">
       <a href="#"><img src="../../img/ext/edward/btn_search_id.png" alt="비밀번호 분실/변경" onclick="chkPassword();"></a>
    </li>
    <li class="pw_find">
      <a href="#"><img src="../../img/ext/edward/btn_search_num.png" alt="학번찾기" onclick="findClassNum();"></a>
    </li>
   </ul>
   
   </div>
   <!-- 알아두어야할 사항 E-->
   
   
   </div>

  
</div>
<!-- //전체감싸기 -->
  </body>
</html>
"""

soup=B(html, 'lxml')

print(soup.find('p'))
print(soup.find_all('p', limit=10))
