from app import create_app

application = create_app()


html = '''
<html>
    <head>
        <title>LogoAliAPI</title>
    </head>
    <body>
        <h1>LogoAliAPI!</h1>
    </body>
</html>
'''
application.add_url_rule('/', 'index', (lambda:html))

application.run()