from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Nexus API Dashboard</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f8fafc;
                    margin: 0;
                    padding: 40px;
                }

                .container {
                    max-width: 900px;
                    margin: 0 auto;
                    background: #ffffff;
                    border-radius: 16px;
                    padding: 30px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
                }

                h1 {
                    margin-top: 0;
                    color: #0f172a;
                }

                p {
                    color: #475569;
                }

                ul {
                    list-style: none;
                    padding: 0;
                }

                li {
                    margin: 12px 0;
                }

                a {
                    display: block;
                    padding: 12px 16px;
                    background: #eff6ff;
                    color: #2563eb;
                    text-decoration: none;
                    border-radius: 10px;
                    font-size: 18px;
                }

                a:hover {
                    background: #dbeafe;
                }

                .footer {
                    margin-top: 24px;
                    font-size: 14px;
                    color: #94a3b8;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Nexus API Dashboard</h1>
                <p>Barcha modullar bitta sahifada:</p>

                <ul>
                    <li><a href="/api/users/register/">🔐 Users - Register</a></li>
                    <li><a href="/api/users/login/">🔑 Users - Login</a></li>
                    <li><a href="/api/users/profile/">👤 Users - Profile</a></li>

                    <li><a href="/api/shop/">🛍️ Shop</a></li>
                    <li><a href="/api/social/">💬 Social</a></li>
                    <li><a href="/api/courses/">🎓 Courses</a></li>
                    <li><a href="/api/chat/">💭 Chat</a></li>
                    <li><a href="/api/payments/">💳 Payments</a></li>
                </ul>

                <div class="footer">
                    Nexus Super Backend Project
                </div>
            </div>
        </body>
        </html>
    """)
