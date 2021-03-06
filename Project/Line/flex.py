from datetime import datetime

tr = True

def FlexDetailTask(subject,detail,deadline,member,userOrder):

    message = {
        "type": "flex",
        "altText": "รายละเอียดสั่งงาน",
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "flex": 0,
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "none",
                    "contents": [
                    {
                        "type": "icon",
                        "url": "https://sv1.picz.in.th/images/2021/02/03/o7JGL1.png",
                        "size": "md"
                    },
                    {
                        "type": "text",
                        "text": "รายละเอียดงาน",
                        "weight": "bold",
                        "size": "lg",
                        "color": "#FF5A1BFF",
                        "align": "start",
                        "margin": "none",
                        "offsetStart": "10px",
                        "contents": []
                    }
                    ]
                }
                ]
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "margin": "none",
                "backgroundColor": "#FFFFFFFF",
                "contents": [
                {
                    "type": "text",
                    "text": subject,
                    "weight": "bold",
                    "size": "md",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "text",
                    "text": detail,
                    "size": "md",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "separator",
                    "margin": "xs",
                    "color": "#E8E8E8FF"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ผู้สั่งงาน :",
                        "weight": "bold",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "@{}".format(userOrder),
                        "align": "end",
                        "contents": []
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ผู้รับผิดชอบ :",
                        "weight": "bold",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "{}".format("@"+" @".join(member)),
                        "size": "md",
                        "align": "end",
                        "wrap": True,
                        "contents": []
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "กำหนดส่ง:",
                        "weight": "bold",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": deadline,
                        "weight": "bold",
                        "size": "md",
                        "align": "end",
                        "wrap": True,
                        "contents": []
                    }
                    ]
                }
                ]
            },
            "styles": {
                "header": {
                "backgroundColor": "#FFD38AFF"
                }
            }
            }
        }
    return message

def FlexRmd():
    message = {
                "type": "flex",
                "altText": "คำแนะนำในการใช้งาน",
                "contents": {
                    "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2020/11/22/bF708q.jpg",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "16:5"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                        {
                            "type": "text",
                            "text": "คำสั่งในการสั่งงาน",
                            "size": "lg",
                            "color": "#ffb75e",
                            "flex": 0,
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#สั่งงาน @name #งาน รายละเอียดงาน",
                            "size": "sm",
                            "color": "#ffffff"
                        },
                        {
                            "type": "text",
                            "text": "#ส่ง วัน/เดือน",
                            "size": "sm",
                            "color": "#ffffff"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "คำสั่งดูงานที่ต้องทำ",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#งานที่ต้องทำ",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "คำสั่งดูงานที่สั่ง",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#งานที่สั่ง",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff",
                            "weight": "regular"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "คำสั่งยกเลิกการสั่งงาน",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#ยกเลิก และกดที่ชื่องานเพื่อยกเลิก",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff",
                            "weight": "regular"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "คำสั่งดูประวัติงาน",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "#ประวัติงาน",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff",
                            "weight": "regular"
                        },
                        {
                            "type": "separator",
                            "margin": "lg",
                            "color": "#ff864a"
                        },
                        {
                            "type": "text",
                            "text": "ตรวจสอบงานผ่านเว็บไซต์",
                            "margin": "lg",
                            "color": "#ffb75e",
                            "size": "lg",
                            "weight": "bold"
                        },
                        {
                            "type": "text",
                            "text": "https://kmitl-chatbot.herokuapp.com",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff"
                        }
                        ]
                    }
                    ],"backgroundColor": "#454545"
                    }
                }
                
            }

    return message
    
## แสดงงานที่ต้องทำ
def FlexMyTask(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "งานที่ต้องทำ",
                    "contents": {
                        "type": "bubble",
                        "size": "kilo",
                        "direction": "ltr",
                        "hero": {
                            "type": "image",
                            "url": "https://sv1.picz.in.th/images/2020/11/16/bH6Ira.jpg",
                            "margin": "none",
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "16:5",
                            "backgroundColor": "#FFB657"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "backgroundColor": "#454545",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "md",
                                "paddingStart": "10px",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "คุณยังไม่มีงานที่ต้องทำ",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#FFFFFFFF",
                                    "align": "center",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "spacer",
                                    "size": "lg"
                                }
                                ]
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 0,
                            "spacing": "sm",
                            "margin": "sm",
                            "contents": [
                            {
                                "type": "text",
                                "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                "weight": "bold",
                                "size": "md",
                                "margin": "md",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "https://kmitl-chatbot.herokuapp.com",
                                "action": {
                                    "type": "uri",
                                    "uri": "https://kmitl-chatbot.herokuapp.com"
                                },
                                "contents": []
                            }
                            ]
                        }
                        }
        }
    else:
        message = {
            "type": "flex",
            "altText": "งานที่ต้องทำ",
            "contents": {
                "type": "bubble",
                "size": "kilo",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2020/11/16/bH6Ira.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFFFF",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่องาน",
                            "weight": "bold",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "กำหนดส่ง",
                            "weight": "bold",
                            "align": "end",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "xs",
                        "margin": "sm",
                        "contents": task
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "none",
                    "offsetBottom": "10px",
                    "paddingStart": "20px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "*เลยกำหนดส่งงาน",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FF4646FF",
                        "margin": "xs",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }

    return message

def FlexFollowTask(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "งานที่สั่ง",
                    "contents": {
                            "type": "bubble",
                            "size": "kilo",
                            "direction": "ltr",
                            "hero": {
                                "type": "image",
                                "url": "https://sv1.picz.in.th/images/2020/11/22/bF7S7z.jpg",
                                "margin": "none",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "16:5",
                                "backgroundColor": "#FFB657"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "backgroundColor": "#454545",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "md",
                                    "paddingStart": "10px",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "คุณยังไม่มีการสั่งงาน",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#FFFFFFFF",
                                        "align": "center",
                                        "margin": "md",
                                        "contents": []
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "lg"
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "margin": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                    "weight": "bold",
                                    "size": "md",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "https://kmitl-chatbot.herokuapp.com",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://kmitl-chatbot.herokuapp.com"
                                    },
                                    "contents": []
                                }
                                ]
                            }
                    }
            }
    else:
        message = {
            "type": "flex",
            "altText": "งานที่สั่ง",
            "contents": {
                "type": "bubble",
                "size": "kilo",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2020/11/22/bF7S7z.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFFFF",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่องาน",
                            "weight": "bold",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "กำหนดส่ง",
                            "weight": "bold",
                            "align": "end",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "xs",
                        "margin": "sm",
                        "contents": task
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "none",
                    "offsetBottom": "10px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "คลิ๊กที่ชื่องานเพื่อดูรายละเอียด",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#FF5050FF",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "sm",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }
    return message


def FlexRejectTask(task,user):
    
    message = {"type": "flex",
                    "altText": "งานที่ยกเลิก",
                    "contents": {
                                "type": "bubble",
                                "hero": {
                                    "type": "image",
                                    "url": "https://sv1.picz.in.th/images/2020/11/18/bXAHd8.jpg",
                                    "size": "full",
                                    "aspectRatio": "16:5",
                                    "aspectMode": "cover"
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "backgroundColor": "#454545",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "backgroundColor": "#454545",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": task["task"],
                                            "weight": "bold",
                                            "size": "xl",
                                            "color": "#FFB75E",
                                            "flex": 0,
                                            "wrap": False,
                                            "align": "start",
                                            "margin": "md",
                                            "contents": []
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "md",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "ผู้รับผิดชอบงาน",
                                                "weight": "bold",
                                                "size": "md",
                                                "color": "#FFFFFFFF",
                                                "align": "start",
                                                "margin": "lg",
                                                "contents": []
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "xs",
                                                "contents": user
                                            }
                                            ]
                                        }
                                        ]
                                    }
                                    ]
                                }
                        }}

    return message

## แสดงงานภายในวันนี้
def FlexTaskToday(task):
    if not task:
        message = {
            "type": "flex",
            "altText": "งานภายในวันนี้",
            "contents": {
                "type": "bubble",
                "size": "kilo",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/01/17/lbZII2.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#454545",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "none",
                        "paddingStart": "10px",
                        "contents": [
                        {
                            "type": "spacer"
                        },
                        {
                            "type": "text",
                            "text": "คุณไม่มีงานที่ต้องส่งภายในวันนี้",
                            "weight": "bold",
                            "color": "#FFFFFFFF",
                            "align": "center",
                            "contents": []
                        },
                        {
                            "type": "spacer"
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "xs",
                    "margin": "sm",
                    "paddingStart": "20px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }
    else:
        message = {
            "type": "flex",
            "altText": "งานภายในวันนี้",
            "contents": {
                "type": "bubble",
                "size": "mega",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/01/17/lbZII2.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#454545",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "none",
                        "paddingStart": "10px",
                        "contents": task
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "xs",
                    "margin": "sm",
                    "paddingStart": "20px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }
    return message
    


def FlexFollowTaskReject(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "งานที่สามารถยกเลิก",
                    "contents": {
                            "type": "bubble",
                            "size": "kilo",
                            "direction": "ltr",
                            "hero": {
                                "type": "image",
                                "url": "https://sv1.picz.in.th/images/2020/11/18/bXAHd8.jpg",
                                "margin": "none",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "16:5",
                                "backgroundColor": "#FFB657"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "backgroundColor": "#454545",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "md",
                                    "paddingStart": "10px",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "ไม่มีมีงานให้ยกเลิก",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#FFFFFFFF",
                                        "align": "center",
                                        "margin": "md",
                                        "contents": []
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "lg"
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "margin": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                    "weight": "bold",
                                    "size": "md",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "https://kmitl-chatbot.herokuapp.com",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://kmitl-chatbot.herokuapp.com"
                                    },
                                    "contents": []
                                }
                                ]
                            }
                    }
            }
    else:
        message = {
            "type": "flex",
            "altText": "งานที่สามารถยกเลิก",
            "contents": {
                "type": "bubble",
                "size": "kilo",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2020/11/18/bXAHd8.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#FFFFFFFF",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่องาน",
                            "weight": "bold",
                            "align": "start",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "กำหนดส่ง",
                            "weight": "bold",
                            "align": "end",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "xs",
                        "margin": "sm",
                        "contents": task
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "none",
                    "offsetBottom": "10px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "คลิ๊กที่ชื่องานเพื่อทำรายการ",
                        "weight": "bold",
                        "size": "sm",
                        "color": "#FF5050FF",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "sm",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }
    return message

## ประวัติงาน
def HistoryTask(task):

    if not task:
        message = {
            "type": "flex",
                    "altText": "ประวัติการทำงาน",
                    "contents": {
                            "type": "bubble",
                            "size": "kilo",
                            "direction": "ltr",
                            "hero": {
                                "type": "image",
                                "url": "https://sv1.picz.in.th/images/2020/11/22/byVouW.jpg",
                                "margin": "none",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "16:5",
                                "backgroundColor": "#FFB657"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "backgroundColor": "#454545",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "md",
                                    "paddingStart": "10px",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "คุณยังไม่มีประวัติการทำงาน",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#FFFFFFFF",
                                        "align": "center",
                                        "margin": "md",
                                        "contents": []
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "lg"
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "margin": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                    "weight": "bold",
                                    "size": "md",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "https://kmitl-chatbot.herokuapp.com",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://kmitl-chatbot.herokuapp.com"
                                    },
                                    "contents": []
                                }
                                ]
                            }
                    }
            }
    else:
        
        message = {
            "type": "flex",
                    "altText": "ประวัติการทำงาน",
                    "contents": {
                        "type": "bubble",
                        "size": "kilo",
                        "direction": "ltr",
                        "hero": {
                            "type": "image",
                            "url": "https://sv1.picz.in.th/images/2020/11/22/byVouW.jpg",
                            "margin": "none",
                            "size": "full",
                            "aspectRatio": "16:5",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "backgroundColor": "#454545",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "backgroundColor": "#454545",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "ชื่องาน",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#FFB75E",
                                    "flex": 0,
                                    "align": "start",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "สถานะ",
                                    "weight": "bold",
                                    "size": "lg",
                                    "color": "#FFB75E",
                                    "align": "end",
                                    "contents": []
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "none",
                                "paddingStart": "10px",
                                "contents": task
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 0,
                            "spacing": "xs",
                            "margin": "sm",
                            "paddingStart": "20px",
                            "contents": [
                            {
                                "type": "text",
                                "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                "weight": "bold",
                                "size": "md",
                                "margin": "sm",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "https://kmitl-chatbot.herokuapp.com",
                                "action": {
                                    "type": "uri",
                                    "uri": "https://kmitl-chatbot.herokuapp.com"
                                },
                                "contents": []
                            }
                            ]
                        }
                        }
        }

    return message


# ตามงาน
def FlexFollow(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "ตามงาน",
                    "contents": {
                            "type": "bubble",
                            "size": "kilo",
                            "direction": "ltr",
                            "hero": {
                                "type": "image",
                                "url": "https://sv1.picz.in.th/images/2020/11/22/bF7S7z.jpg",
                                "margin": "none",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "16:5",
                                "backgroundColor": "#FFB657"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "backgroundColor": "#454545",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "md",
                                    "paddingStart": "10px",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "คุณยังไม่มีการสั่งงาน",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#FFFFFFFF",
                                        "align": "center",
                                        "margin": "md",
                                        "contents": []
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "lg"
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "margin": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                    "weight": "bold",
                                    "size": "md",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "https://kmitl-chatbot.herokuapp.com",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://kmitl-chatbot.herokuapp.com"
                                    },
                                    "contents": []
                                }
                                ]
                            }
                    }
            }
    else:
        message = {
            "type": "flex",
                    "altText": "ตามงาน",
                    "contents": {
                "type": "bubble",
                "size": "mega",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/01/11/lZ4Ttn.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#454545",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "backgroundColor": "#454545",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่องาน",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#FFB75E",
                            "flex": 0,
                            "align": "start",
                            "margin": "md",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "กำหนดส่ง",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#FFB75E",
                            "align": "end",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "none",
                        "paddingStart": "10px",
                        "contents": task
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "xs",
                    "margin": "sm",
                    "paddingStart": "20px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "*เลยกำหนดส่งงาน",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FF4646FF",
                        "margin": "xs",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }
    return message


## รายการรอตรวจสอบ
def FlexReviewTask(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "ตรวจงาน",
                    "contents": {
                            "type": "bubble",
                            "size": "kilo",
                            "direction": "ltr",
                            "hero": {
                                "type": "image",
                                "url": "https://sv1.picz.in.th/images/2020/11/22/byVDI2.jpg",
                                "margin": "none",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "16:5",
                                "backgroundColor": "#FFB657"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "backgroundColor": "#454545",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "md",
                                    "paddingStart": "10px",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "คุณยังไม่มีงานที่ต้องตรวจ",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#FFFFFFFF",
                                        "align": "center",
                                        "margin": "md",
                                        "contents": []
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "lg"
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "margin": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                    "weight": "bold",
                                    "size": "md",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "https://kmitl-chatbot.herokuapp.com",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://kmitl-chatbot.herokuapp.com"
                                    },
                                    "contents": []
                                }
                                ]
                            }
                    }
            }
    else:
        message = {
            "type": "flex",
                    "altText": "ตรวจงาน",
                    "contents": {
                "type": "bubble",
                "size": "mega",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2020/11/22/byVDI2.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#454545",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "backgroundColor": "#454545",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่องาน",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#FFB75E",
                            "flex": 0,
                            "align": "start",
                            "margin": "md",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "กำหนดส่ง",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#FFB75E",
                            "align": "end",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "none",
                        "paddingStart": "10px",
                        "contents": task
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "xs",
                    "margin": "sm",
                    "paddingStart": "20px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }
    return message

# ส่งงาน
def FlexTaskList(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "ส่งงาน",
                    "contents": {
                            "type": "bubble",
                            "size": "kilo",
                            "direction": "ltr",
                            "hero": {
                                "type": "image",
                                "url": "https://sv1.picz.in.th/images/2021/01/11/lZ43IS.jpg",
                                "margin": "none",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "16:5",
                                "backgroundColor": "#FFB657"
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "backgroundColor": "#454545",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "md",
                                    "paddingStart": "10px",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "คุณยังไม่มีการสั่งงาน",
                                        "weight": "bold",
                                        "size": "lg",
                                        "color": "#FFFFFFFF",
                                        "align": "center",
                                        "margin": "md",
                                        "contents": []
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "lg"
                                    }
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "margin": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                                    "weight": "bold",
                                    "size": "md",
                                    "margin": "md",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "https://kmitl-chatbot.herokuapp.com",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://kmitl-chatbot.herokuapp.com"
                                    },
                                    "contents": []
                                }
                                ]
                            }
                    }
            }
    else:
        message = {
            "type": "flex",
                    "altText": "ส่งงาน",
                    "contents": {
                "type": "bubble",
                "size": "mega",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/01/11/lZ43IS.jpg",
                    "margin": "none",
                    "size": "full",
                    "aspectRatio": "16:5",
                    "aspectMode": "cover",
                    "backgroundColor": "#FFB657"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "backgroundColor": "#454545",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "backgroundColor": "#454545",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่องาน",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#FFB75E",
                            "flex": 0,
                            "align": "start",
                            "margin": "md",
                            "contents": []
                        },
                        {
                            "type": "text",
                            "text": "กำหนดส่ง",
                            "weight": "bold",
                            "size": "lg",
                            "color": "#FFB75E",
                            "align": "end",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "none",
                        "paddingStart": "10px",
                        "contents": task
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "flex": 0,
                    "spacing": "xs",
                    "margin": "sm",
                    "paddingStart": "20px",
                    "contents": [
                    {
                        "type": "text",
                        "text": "*เลยกำหนดส่งงาน",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FF4646FF",
                        "margin": "xs",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "สามารถตรวจสอบงานเพิ่มเติมได้ที่",
                        "weight": "bold",
                        "size": "md",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "https://kmitl-chatbot.herokuapp.com",
                        "action": {
                            "type": "uri",
                            "uri": "https://kmitl-chatbot.herokuapp.com"
                        },
                        "contents": []
                    }
                    ]
                }
                }
        }
    return message

# response ตามงาน
def BubbleFollow(task):
    deadline = datetime.strftime(task["deadline"],"%d %b, %Y")
    info = (task["task"][:50] + '..') if len(task["task"]) > 75 else task["task"]

    message = {
        "type": "flex",
        "altText": "ตามงาน",
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "กรุณาส่งงาน",
                    "weight": "bold",
                    "size": "xl",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "flex": 1,
                    "margin": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": task["task"],
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0,
                        "wrap": False,
                        "contents": []
                    }
                    ]
                },
                {
                    "type": "text",
                    "text": "กำหนดส่ง: "+deadline,
                    "size": "sm",
                    "color": "#FF5551",
                    "flex": 0,
                    "margin": "md",
                    "wrap": True,
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "Send Work",
                        "text": "ยืนยันการส่งงาน\n{}\nเรียบร้อย".format(info),
                        "data": "action=send&id={}".format(str(task["_id"]))
                    },
                    "color": "#FF9B00FF",
                    "style": "primary"
                }
                ]
            }
            }
    }

    return message

## ข้อมูลก่อนกดส่งงาน
def BubbleInfoTask(task):

    deadline = datetime.strftime(task["deadline"],"%d %b, %Y")
    info = (task["task"][:50] + '..') if len(task["task"]) > 75 else task["task"]

    message = {
        "type": "flex",
        "altText": "ข้อมูลก่อนส่งงาน",
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "รายละเอียดงาน",
                    "weight": "bold",
                    "size": "xl",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "flex": 1,
                    "margin": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": task["task"],
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0,
                        "wrap": False,
                        "contents": []
                    }
                    ]
                },
                {
                    "type": "text",
                    "text": "ผู้สั่งงาน: "+task["order_by"],
                    "size": "sm",
                    "color": "#FF5551",
                    "flex": 0,
                    "margin": "md",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "text",
                    "text": "กำหนดส่ง: "+deadline,
                    "size": "sm",
                    "color": "#FF5551",
                    "flex": 0,
                    "margin": "md",
                    "wrap": True,
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "Send Work",
                        "text": "ยืนยันการส่งงาน\n{}\nเรียบร้อยแล้ว".format(info),
                        "data": "action=send&id={}".format(str(task["_id"]))
                    },
                    "color": "#FF9B00FF",
                    "style": "primary"
                }
                ]
            }
            }
    }

    return message


# ข้อมุลก่อนยกเลิกงาน
def BubbleInfoBeforeCancel(task):
    deadline = datetime.strftime(task["deadline"],"%d %b, %Y")
    info = (task["task"][:50] + '..') if len(task["task"]) > 75 else task["task"]
    message = {
        "type": "flex",
        "altText": "ข้อมูลก่อนส่งงาน",
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "ยืนยันการยกเลิกงาน",
                    "weight": "bold",
                    "size": "xl",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "flex": 1,
                    "margin": "md",
                    "contents": [
                    {
                        "type": "text",
                        "text": task["task"],
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0,
                        "wrap": False,
                        "contents": []
                    }
                    ]
                },
                {
                    "type": "text",
                    "text": "กำหนดส่ง: {}".format(deadline),
                    "size": "sm",
                    "color": "#FF5551",
                    "flex": 0,
                    "margin": "md",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "text",
                    "text": "ผู้รับผิดชอบ: {}".format("@"+" @".join(task["member"])),
                    "size": "sm",
                    "color": "#FF5551",
                    "flex": 0,
                    "margin": "md",
                    "wrap": True,
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "postback",
                        "label": "Delete Work",
                        "text": "ยืนยันการยกเลิกงาน\n{}\nผู้รับผิดชอบ: {}".format(info,"@"+" @".join(task["member"])),
                        "data": "action=remove&id={}".format(str(task["_id"]))
                    },
                    "color": "#F04E4EFF",
                    "style": "primary"
                }
                ]
            }
        }
    }



    return message


## แสดง Accept Reject ตรวจงาน
def BubbleReviewTask(task):
    info = (task["task"][:50] + '..') if len(task["task"]) > 75 else task["task"]

    message = {
        "type": "flex",
        "altText": "มีงานส่งมาจาก {}".format("@"+" @".join(task["member"])),
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "direction": "ltr",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "backgroundColor": "#454545",
                "contents": [
                {
                    "type": "text",
                    "text": "ตรวจงาน : {}".format(task["task"]),
                    "color": "#FFFFFFFF",
                    "wrap": False,
                    "contents": []
                },
                {
                    "type": "text",
                    "text": "ผู้รับผิดชอบ : {}".format("@"+" @".join(task["member"])),
                    "color": "#FFFFFFFF",
                    "wrap": True,
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "flex": 0,
                "spacing": "xs",
                "margin": "sm",
                "paddingStart": "20px",
                "backgroundColor": "#FFFFFFFF",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "Reject",
                            "text": "ตรวจสอบการส่งงาน {}".format(info),
                            'data': "action=reject&id={}".format(task["_id"])
                        },
                        "color": "#C93131FF",
                        "height": "md",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "Accept",
                            "text": "ตรวจสอบการส่งงาน {}".format(info),
                            'data': "action=accept&id={}".format(task["_id"])
                        },
                        "height": "md",
                        "style": "primary"
                    }
                    ]
                }
                ]
            }
            }
    }

    return message

def BubbleAcceptRejectTask(task):
    info = (task["task"][:50] + '..') if len(task["task"]) > 75 else task["task"]
    message = {
        "type": "flex",
        "altText": "ตรวจงาน"+ info,
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "direction": "ltr",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "backgroundColor": "#454545",
                "contents": [
                {
                    "type": "text",
                    "text": "ตรวจงาน : {}".format(task["task"]),
                    "color": "#FFFFFFFF",
                    "wrap": False,
                    "contents": []
                },
                {
                    "type": "text",
                    "text": "ผู้รับผิดชอบ : {}".format("@"+" @".join(task["member"])),
                    "color": "#FFFFFFFF",
                    "wrap": True,
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "flex": 0,
                "spacing": "xs",
                "margin": "sm",
                "paddingStart": "20px",
                "backgroundColor": "#FFFFFFFF",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "Reject",
                            "text": "ตรวจสอบการส่งงาน {}".format(info),
                            'data': "action=reject&id={}".format(task["_id"])
                        },
                        "color": "#C93131FF",
                        "height": "md",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                            "type": "postback",
                            "label": "Accept",
                            "text": "ตรวจสอบการส่งงาน {}".format(task["task"]),
                            'data': "action=accept&id={}".format(task["_id"])
                        },
                        "height": "md",
                        "style": "primary"
                    }
                    ]
                }
                ]
            }
            }
    }

    return message

def FlexAssignTask(profile,groupId):

    message = {
        "type": "flex",
        "altText": "เริ่มการสั่งงาน",
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "text",
                    "text": "เริ่มต้นการสั่งงาน",
                    "weight": "bold",
                    "size": "xl",
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "text",
                    "text": "ผู้สั่งงาน: "+profile,
                    "size": "sm",
                    "color": "#FF5551",
                    "flex": 0,
                    "margin": "md",
                    "wrap": True,
                    "contents": []
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "สั่งงาน",
                        "uri": "https://liff.line.me/1654805076-agyLkygK/?gid={}".format(groupId)
                    },
                    "color": "#FF9B00FF",
                    "style": "primary"
                }
                ]
            }
            }
    }

    return message


## เมนูแนะนำคำสั่ง BOT
def Menu():
   
    message = {
        "type": "flex",
        "altText": "คำแนะนำการใช้งาน",
        "contents": {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "size": "kilo",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/12/oK6dm9.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover"
                }
                },
                {
                "type": "bubble",
                "size": "kilo",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/12/oK6UyN.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover"
                }
                },
                {
                "type": "bubble",
                "size": "kilo",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/12/oK6QsE.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover"
                }
                }
            ]
            }
    }

    return message


## say jeny one-one
def CommandBot():
    message = {
        "type": "flex",
        "altText": "Hello Jeny !",
        "contents": {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgSKP.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgYPt.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type": "message",
                        "text": "#งานที่สั่ง"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUg7WI.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type": "message",
                        "text": "#งานที่ต้องทำ"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgN3l.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type": "message",
                        "text": "#ตามงาน"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUg3QN.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type": "message",
                        "text": "#ส่งงาน"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgzee.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type":"postback",
                        "text":"ตรวจงาน",
                        "data":"action=check"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgfav.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type": "message",
                        "text": "#ยกเลิก"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgBbk.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type": "message",
                        "text": "#ประวัติงาน"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgk4E.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type":"uri",
                        "uri":"https://kmitl-chatbot.herokuapp.com"
                    }
                }
                }
            ]
            }
    }

    return message

## when say jeny carousel in group
def CommandBotInGroup(groupID):
    message = {
        "type": "flex",
        "altText": "Hello Jeny !",
        "contents": {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgSKP.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover"
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUg9nV.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type":"postback",
                        "label":"สั่งงาน",
                        "text": "สั่งงาน",
                        "data": "action=assign&groupId={}".format(groupID)
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgYPt.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type" : "message",
                        "text": "#งานที่สั่ง"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUg7WI.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type" : "message",
                        "text": "#งานที่ต้องทำ"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgfav.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type" : "message",
                        "text": "#ยกเลิก"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgBbk.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type" : "message",
                        "text": "#ประวัติงาน"
                    }
                }
                },
                {
                "type": "bubble",
                "size": "micro",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2021/02/16/oUgk4E.jpg",
                    "size": "full",
                    "aspectRatio": "11:12",
                    "aspectMode": "cover",
                    "action": {
                        "type":"uri",
                        "uri":"https://kmitl-chatbot.herokuapp.com"
                    }
                }
                }
            ]
            }
    }

    return message

def QuickReply():

    message = {
            "items":[
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbUsKf.png",
                    "action": {
                        "type":"message",
                        "label":"คำสั่งแนะนำ",
                        "text":"#คำสั่งแนะนำ"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbqMGz.png",
                    "action": {
                        "type":"message",
                        "label":"งานที่สั่ง",
                        "text":"#งานที่สั่ง"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbqaB1.png",
                    "action": {
                        "type":"message",
                        "label":"งานที่ต้องทำ",
                        "text":"#งานที่ต้องทำ"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbqIlq.png",
                    "action": {
                        "type":"message",
                        "label":"ตามงาน",
                        "text":"#ตามงาน"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb5IMQ.png",
                    "action": {
                        "type":"message",
                        "label":"ส่งงาน",
                        "text":"#ส่งงาน"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb50qR.png",
                    "action": {
                        "type":"message",
                        "label":"ยกเลิกงาน",
                        "text":"#ยกเลิก"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/29/lJvq9k.png",
                    "action": {
                        "type":"postback",
                        "label":"ตรวจงาน",
                        "text":"ตรวจงาน",
                        "data":"action=check"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb5pJe.png",
                    "action": {
                        "type":"message",
                        "label":"ประวัติงาน",
                        "text":"#ประวัติงาน"
                    }
                },
                {
                    "type":"action",
                    "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb5dB8.png",
                    "action": {
                        "type":"message",
                        "label":"ตรวจสอบงานผ่านเว็บไซต์",
                        "text":"สามารถตรวจสอบงานเพิ่มเติมได้ที่\nhttps://kmitl-chatbot.herokuapp.com/"
                    }
                }
            ]
        }
    
    return message


def QuickReplyGroup(groupID):
    message = {
                    "items":[
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbUsKf.png",
                            "action": {
                                "type":"message",
                                "label":"คำสั่งแนะนำ",
                                "text":"#คำสั่งแนะนำ"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbEczR.png",
                            "action": {
                                "type":"postback",
                                "label":"สั่งงาน",
                                "text": "สั่งงาน",
                                "data": "action=assign&groupId={}".format(groupID)
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbqMGz.png",
                            "action": {
                                "type":"message",
                                "label":"งานที่สั่ง",
                                "text":"#งานที่สั่ง"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lbqaB1.png",
                            "action": {
                                "type":"message",
                                "label":"งานที่ต้องทำ",
                                "text":"#งานที่ต้องทำ"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb50qR.png",
                            "action": {
                                "type":"message",
                                "label":"ยกเลิกงาน",
                                "text":"#ยกเลิก"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb5pJe.png",
                            "action": {
                                "type":"message",
                                "label":"ประวัติงาน",
                                "text":"#ประวัติงาน"
                            }
                        },
                        {
                            "type":"action",
                            "imageUrl": "https://sv1.picz.in.th/images/2021/01/18/lb5dB8.png",
                            "action": {
                                "type":"message",
                                "label":"ตรวจสอบงานผ่านเว็บไซต์",
                                "text":"สามารถตรวจสอบงานเพิ่มเติมได้ที่\nhttps://kmitl-chatbot.herokuapp.com/"
                            }
                        }
                    ]
                }


    return message

def FlexInformation(task):

    member = ' '.join(task["member"])
    deadline_obj = task["deadline"]
    deadline_str = "{}/{}/{}".format(str(deadline_obj.day), str(deadline_obj.month), str(deadline_obj.year))
    message = {
        "type": "flex",
        "altText": "รายละเอียดงาน {}".format(task["task"]),
        "contents": {
        "type": "bubble",
        "size": "kilo",
        "direction": "ltr",
        "header": {
            "type": "box",
            "layout": "vertical",
            "flex": 0,
            "backgroundColor": "#454545FF",
            "contents": [
            {
                "type": "text",
                "text": task["task"],
                "size": "lg",
                "color": "#FFFFFFFF",
                "wrap": False,
                "contents": []
            }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "none",
            "margin": "none",
            "backgroundColor": "#454545",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "backgroundColor": "#454545",
                "contents": [
                {
                    "type": "text",
                    "text": task["detail"],
                    "weight": "bold",
                    "size": "md",
                    "color": "#FFB27B",
                    "flex": 0,
                    "wrap": True,
                    "contents": []
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "ผู้รับผิดชอบงาน",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFFFFFFF",
                        "align": "start",
                        "margin": "lg",
                        "contents": []
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xs",
                        "contents": [
                        {
                            "type": "text",
                            "text": member,
                            "weight": "bold",
                            "size": "md",
                            "color": "#FFB27B",
                            "align": "start",
                            "margin": "sm",
                            "wrap": True,
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "กำหนดส่งงาน",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFFFFFFF",
                        "margin": "lg",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": deadline_str,
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFB27B",
                        "margin": "sm",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "ผู้สั่งงาน",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFFFFFFF",
                        "margin": "md",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": task["order_by"],
                        "weight": "bold",
                        "size": "md",
                        "color": "#FFB27B",
                        "margin": "sm",
                        "contents": []
                    }
                    ]
                }
                ]
            }
            ]
        },
        "styles": {
            "header": {
            "separatorColor": "#FFFFFFFF"
            },
            "body": {
            "backgroundColor": "#FFFFFFFF",
            "separator": True
            }
        }
        }
    }
    return message