
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

boss@server:~/git/docker$ cd git
bash: cd: git: No such file or directory
boss@server:~/git/docker$ cd
boss@server:~$ cd git
boss@server:~/git$ nano main.py
  GNU nano 6.2                                      main.py *
from io import BytesIO

app = Flask(__name__)

@app.route("/qr")
def qr():
   msg = request.args.get('msg')
   img = qrcode.make(msg)

   buffer = BytesIO()
   img.save(buffer, format="png")




