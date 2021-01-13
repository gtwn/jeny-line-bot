from datetime import datetime

tr = True

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
                            "text": "www..",
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


def FlexFollowTaskReject(task):
    if not task:
        message = {
            "type": "flex",
                    "altText": "งานที่สามารถยกเลิก",
                    "contents": {
                            "type": "bubble",
                            "size": "mega",
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
                    "altText": "งานที่สามารถยกเลิก",
                    "contents": {
                "type": "bubble",
                "size": "mega",
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


def HistoryTask(task):

    if not task:
        message = {
            "type": "flex",
                    "altText": "ประวัติการทำงาน",
                    "contents": {
                            "type": "bubble",
                            "size": "mega",
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
                    "altText": "ประวัติการทำงาน",
                    "contents": {
                        "type": "bubble",
                        "size": "giga",
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
                                "text": "www.",
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
                            "size": "mega",
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
                        "text": "www.",
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
                            "size": "mega",
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
                    "altText": "ส่งงาน",
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
                        "text": "www.",
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
                        "wrap": True,
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
                    "type": "message",
                    "label": "Send Work",
                    "text": "#Send "+str(task["_id"])+" "+task["task"]
                    },
                    "color": "#FF9B00FF",
                    "style": "primary"
                }
                ]
            }
            }
    }

    return message


def BubbleInfoTask(task):
    deadline = datetime.strftime(task["deadline"],"%d %b, %Y")

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
                        "wrap": True,
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
                    "type": "message",
                    "label": "Send Work",
                    "text": "#Send "+str(task["_id"])+" "+task["task"]
                    },
                    "color": "#FF9B00FF",
                    "style": "primary"
                }
                ]
            }
            }
    }

    return message

def BubbleReviewTask(task):
    message = {
        "type": "flex",
        "altText": "มีการส่งงานจาก"+task["order_to"],
        "contents":{
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
                    "text": "ตรวจงาน : "+task["task"],
                    "color": "#FFFFFFFF",
                    "wrap":True,
                    "contents": []
                },
                {
                    "type": "text",
                    "text": "ผู้รับผิดชอบ : "+task["order_to"],
                    "color": "#FFFFFFFF",
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
                        "type": "message",
                        "label": "Reject",
                        "text": "#Reject "+str(task["_id"])+" "+task["task"]
                        },
                        "color": "#C93131FF",
                        "height": "md",
                        "style": "primary"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "Accept",
                        "text": "#Accept "+str(task["_id"])+" "+task["task"]
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



def Menu():
    message = {
    "type": "template",
    "altText": "คำสั่งแนะนำ",
    "template": {
        "type": "image_carousel",
        "columns": [
            {
                "imageUrl": "https://sv1.picz.in.th/images/2020/11/22/bF7S7z.jpg",
                "aspectRatio": "11:12",
                "action": {
                    "type": "message",
                    "text": "#งานที่สั่ง"
                }
            },
            {
                "imageUrl": "https://sv1.picz.in.th/images/2020/11/16/bH6Ira.jpg",
                "aspectRatio": "11:12",
                "action": {
                    "type": "message",
                    "text": "#งานที่ต้องทำ"
                }
            },
            {
                "imageUrl": "https://sv1.picz.in.th/images/2020/11/18/bXAHd8.jpg",
                "aspectRatio": "11:12",
                "action": {
                    "type": "message",
                    "text": "#ยกเลิก"
                }
            },
            {
                "imageUrl": "https://sv1.picz.in.th/images/2020/11/22/byV65J.jpg",
                "aspectRatio": "11:12",
                "action": {
                    "type": "message",
                    "text": "#ส่งงาน"
                }
            },
            {
                "imageUrl": "https://sv1.picz.in.th/images/2021/01/11/lZ4Ttn.jpg",
                "aspectRatio": "11:12",
                "action": {
                    "type": "message",
                    "text": "#ตามงาน"
                }
            },
            {
                "imageUrl": "https://sv1.picz.in.th/images/2020/11/22/byVouW.jpg",
                "aspectRatio": "11:12",
                "action": {
                    "type": "message",
                    "text": "#ประวัติงาน"
                }
            }]
        }
    }

    return message