import cherrypy
import subprocess
class Terminal:
    @cherrypy.expose
    def index(self):
        return """
            <html>
                <head>
                    <title>CherryPy Practice</title>
                    <style>
                        body {
                            font-family: sans-serif;
                            max-width: 800px;
                            margin: 0 auto;
                            margin-top: 8%;
                            background-color: black;
                            text-align: center;  
                            color: white;
                          
                        }
                        form {
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin-top: 20px;
                        }
                        input[type="text"] {
                            width: 70%;
                            padding: 12px 20px;
                            margin: 8px 0;
                            box-sizing: border-box;
                            border: 2px solid #ccc;
                            border-radius: 4px;
                        }
                        button[type="submit"] {
                            width: 30%;
                            background-color: #4CAF50;
                            color: white;
                            padding: 14px 20px;
                            margin: 8px 0;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;
                        }
                      
                        pre {
                            background-color: #FFFFFF;
                            padding: 20px;
                            margin-top: 20px;
                            border-radius: 4px;
                            white-space: pre-wrap;
                        }
                    </style>
                </head>
                <body>

                <h1 > Terminal box</h1>
                    <form method="post" action="execute">
                        <input type="text" name="command" />
                        <button type="submit">Execute Command</button>
                    </form>
                    <div id="output">
                    </div>
                </body>
            </html>
        """








        

    @cherrypy.expose
    def execute(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output
        output = output.decode().replace('\n', '<br>')
        return """
            <html>
                <head>
                    <title>CherryPy Practice</title>
                   
                </head>
                <body style="font-family: sans-serif;
                            max-width: 800px;
                            margin: 0 auto;
                            margin-top: 8%;
                            background-color: black;
                            text-align: center;  
                            color: yellow;">
                <h1 style="color:white;"> Terminal box</h1>
                    <form method="post" action="execute" style="display: flex;
                            align-items: center;
                            justify-content: center;
                            margin-top: 20px;">

                        <input style="width: 70%;
                            padding: 12px 20px;
                            margin: 8px 0;
                            box-sizing: border-box;
                            border: 2px solid #ccc;
                            border-radius: 4px;"
                            type="text" name="command" />
                        <button style="width: 30%;
                            background-color: #4CAF50;
                            color: white;
                            padding: 14px 20px;
                            margin: 8px 0;
                            border: none;
                            border-radius: 4px;
                            cursor: pointer;"
                             type="submit">Execute Command</button>
                    </form>
            <pre><div style="text-align: left; font-size: 16px;">{}</div></pre>
                </body>
            </html>
        """.format(output)

if __name__ == '__main__':
    cherrypy.quickstart(Terminal())
