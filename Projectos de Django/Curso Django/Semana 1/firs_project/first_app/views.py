from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8"/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="icon" type="image/x-icon" href="https://github.githubassets.com/favicons/favicon-dark.png"/>
        <title>Particles</title>
        <meta http-equiv="content-Type" content="text/html; ISO-8859-1">
        <meta name="DC.Language" SCHEME="RFC1766" content="English">
        <meta name="AUTHOR" content="Sergio Luis Beleño Díaz">
        <meta name="copyright" content="Sergio Luis Beleño Díaz" />
        <meta name="REPLY-TO" content="serbeldiaz@gmail.com">
        <LINK REV="made" href="mailto:serbeldiaz@gmail.com">
        <meta name="DESCRIPTION" content="This is a page of particles, try clicking in the page...">
        <meta name="KEYWORDS" content="particles,django,python,html,css,javascript">
        <meta name="Resource-type" content="Homepage">
        <meta name="DateCreated" content="Sun, 23 May 2021 00:00:00 GMT+5">
        <meta name="Revisit-after" content="30 days">
        <meta name="robots" content="INDEX">
    </head>
    
    <body>
        <h1 style="display:none;">Particles</h1>
        <h3 style="display:none;">Particles</h3>
        <div id="particles-js"></div>
        <style>
            /* ESTILOS GENERALES */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
    
            body {
                background-color: #000;
                color: #fff;
                font-size: 18px;
                font-family: 'Lato', sans-serif;
                font-weight: 300;
            }
    
            #particles-js {
                height: 100vh;
                width: 100%;
                position: fixed;
                z-index: -1;
            }
    
            .contenedor {
                width: 90%;
                max-width: 1200px;
                background-size: cover;
                background-image: url('../img/bg-header3.jpeg');
                background-position: center;
                margin-left: auto;
                margin-right: auto;
                margin-top: 15px;
                padding: 20px 30px;
                position: relative;
                z-index: 99;
                opacity: .85;
            }
    
            .contenedor.header {
                height: calc(100vh - 55px);
                border: 3px solid #555555;
            }
    
            .barra-navegacion ul {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
    
            .barra-navegacion li {
                list-style: none;
                display: inline-block;
            }
    
            .barra-navegacion .logo {
                color: #3dff3e;
                font-size: 50px;
            }
    
            .barra-navegacion a {
                text-decoration: none;
                color: #fff;
                font-size: 19px;
                font-family: 'Lato', sans-serif;
                font-weight: 400;
                text-transform: uppercase;
                border-bottom: 1px solid transparent;
                transition: .5s ease;
            }
    
            .barra-navegacion a:hover {
                color: #3dff3e;
                border-bottom: 1px solid currentcolor;
            }
    
            .contenido-descripcion {
                width: 60%;
                display: flex;
                height: 100%;
                align-items: center;
            }
    
            .contenido-descripcion .titulo {
                text-transform: uppercase;
                letter-spacing: 5px;
            }
    
            .contenido-descripcion .titulo span:first-child {
                font-size: 50px;
                display: block;
                font-weight: 300;
            }
    
            .contenido-descripcion .titulo span:last-child {
                font-weight: 900;
                font-size: 100px;
            }
    
            .contenido-descripcion .btn-link {
                display: inline-block;
                padding: 10px 20px;
                margin: 25px 0;
                text-transform: uppercase;
                text-decoration: none;
                color: #3dff3e;
                border: 1px solid #555555;
                animation: parpadeo 2s linear infinite;
                transition: .7s ease;
            }
    
            .contenido-descripcion .btn-link:hover {
                border: 1px solid #3dff3e;
                animation: none;
            }
    
    
            @keyframes parpadeo {
    
                0%,
                41%,
                45%,
                47%,
                49.5%,
                100% {
                    opacity: 1;
                }
    
                42%,
                44%,
                46%,
                48%,
                50% {
                    opacity: 0;
                }
            }
        </style>
        <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.js"></script>
        <script>
            particlesJS({
                "particles": {
                    "number": {
                        "value": 100,
                        "density": {
                            "enable": true,
                            "value_area": 800
                        }
                    },
                    "color": {
                        "value": "#00ff0f"
                    },
                    "shape": {
                        "type": "circle",
                        "stroke": {
                            "width": 0,
                            "color": "#0000ff"
                        },
                        "polygon": {
                            "nb_sides": 5
                        },
                        "image": {
                            "src": "img/github.svg",
                            "width": 100,
                            "height": 100
                        }
                    },
                    "opacity": {
                        "value": 0.5,
                        "random": true,
                        "anim": {
                            "enable": false,
                            "speed": 1,
                            "opacity_min": 0.1,
                            "sync": false
                        }
                    },
                    "size": {
                        "value": 10,
                        "random": true,
                        "anim": {
                            "enable": false,
                            "speed": 40,
                            "size_min": 10.388946161284391,
                            "sync": false
                        }
                    },
                    "line_linked": {
                        "enable": true,
                        "distance": 126.26561550541749,
                        "color": "#00ff0f",
                        "opacity": 0.78916009690886,
                        "width": 1
                    },
                    "move": {
                        "enable": true,
                        "speed": 6,
                        "direction": "none",
                        "random": false,
                        "straight": false,
                        "out_mode": "out",
                        "bounce": false,
                        "attract": {
                            "enable": false,
                            "rotateX": 600,
                            "rotateY": 1200
                        }
                    }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": {
                        "onhover": {
                            "enable": false,
                            "mode": "grab"
                        },
                        "onclick": {
                            "enable": true,
                            "mode": "push"
                        },
                        "resize": true
                    },
                    "modes": {
                        "grab": {
                            "distance": 400,
                            "line_linked": {
                                "opacity": 1
                            }
                        },
                        "bubble": {
                            "distance": 400,
                            "size": 40,
                            "duration": 2,
                            "opacity": 8,
                            "speed": 3
                        },
                        "repulse": {
                            "distance": 200,
                            "duration": 0.4
                        },
                        "push": {
                            "particles_nb": 4
                        },
                        "remove": {
                            "particles_nb": 2
                        }
                    }
                },
                "retina_detect": true
            });
        </script>
    </body>
    
    </html>
    """)