# RSSB_SCM
Selenium Automation Testing

Install VNC Viewer https://www.realvnc.com/en/

Install Docker

docker run -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug

Open 127.0.0.1:5900 on VNC Viewer for viewing the automation tests

docker build -t rssb_scm . --build-arg SITE_LOGIN_USER=&lt;username&gt; --build-arg SITE_LOGIN_PWD=&lt;password&gt; --build-arg CMD_EXECUTOR=http://127.0.0.1:4444/wd/hub

docker run -it --net="host" --env SCM_HOME=/opt/ -v /Users/raj.singh/Home/Work/RSSB/RSSB_SCM/:/opt/ -w /opt/src/main/python rssb_scm python browser.py

docker run -it --net="host" --env SCM_HOME=/opt/ -v /Users/raj.singh/Home/Work/RSSB/RSSB_SCM/:/opt/ -w /opt/src/unittest/python rssb_scm python -m unittest fiddle_tests
