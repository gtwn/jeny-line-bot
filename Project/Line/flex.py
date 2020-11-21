def FlexDetailTask(task,deadline,orderto,user):
    message = {
        "type": "flex",
                "altText": "รายละเอียดสั่งงาน",
                "contents": {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://sv1.picz.in.th/images/2020/11/16/bHnh8t.jpg",
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
                                    "text": task,
                                    "weight": "bold",
                                    "size": "xl",
                                    "color": "#FFB75E",
                                    "flex": 0,
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
                                        "contents": orderto
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
                                        "text": deadline,
                                        "weight": "bold",
                                        "size": "md",
                                        "color": "#F93636FF",
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
                                        "text": '@'+user,
                                        "weight": "bold",
                                        "size": "md",
                                        "color": "#F93636FF",
                                        "margin": "sm",
                                        "contents": []
                                    }
                                    ]
                                }
                                ]
                            }
                            ]
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
                    "url": "https://sv1.picz.in.th/images/2020/11/16/bHCVfS.jpg",
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
                            "text": "#สั่งงาน @name รายละเอียดงาน",
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
                            "text": "#ยกเลิกงาน ชื่องานที่ต้องการยกเลิก @name",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff",
                            "weight": "regular"
                        },
                        {
                            "type": "text",
                            "text": "หรือใช้ #ยกเลิก และกดที่ชื่องานเพื่อยกเลิก",
                            "margin": "md",
                            "size": "sm",
                            "color": "#ffffff",
                            "weight": "regular"
                        }
                        ,
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
                            "text": "www..",
                            "margin": "md",
                            "size": "sm",
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "http://linecorp.com/"
                            },
                            "color": "#ffffff"
                        }
                        ]
                    }
                    ],"backgroundColor": "#454545"
                    }
                }
                
            }

    return message

def FlexMyTask(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "งานที่ต้องทำ",
                    "contents": {
                        "type": "bubble",
                        "size": "mega",
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
                                "text": "www.",
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
                "size": "giga",
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
                        "layout": "baseline",
                        "backgroundColor": "#454545",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ชื่องาน",
                            "weight": "bold",
                            "size": "xl",
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
                            "size": "xl",
                            "color": "#FFB75E",
                            "align": "end",
                            "contents": []
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "md",
                        "paddingStart": "10px",
                        "contents": task
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
                        "text": "*เลยกำหนดส่งงาน",
                        "weight": "bold",
                        "size": "md",
                        "color": "#FF4646FF",
                        "contents": []
                    },
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
                        "text": "www.",
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
                            "size": "mega",
                            "direction": "ltr",
                            "hero": {
                                "type": "image",
                                "url": "https://sv1.picz.in.th/images/2020/11/16/bHnzju.jpg",
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
                                    "text": "www.",
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
                "size": "mega",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": "https://sv1.picz.in.th/images/2020/11/16/bHnzju.jpg",
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
                        "text": "www.",
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
                                            "text": task,
                                            "weight": "bold",
                                            "size": "xl",
                                            "color": "#FFB75E",
                                            "flex": 0,
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