def FlexDetailTask(task,deadline,orderto,user):
    message = {
        "type": "flex",
                "altText": "Flex Message",
                "contents": {
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://sv1.picz.in.th/images/2020/11/16/bHnh8t.jpg",
                        "size": "full",
                        "aspectRatio": "20:13",
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
                                    "type": "text",
                                    "text": orderto,
                                    "weight": "bold",
                                    "size": "md",
                                    "color": "#F93636FF",
                                    "align": "start",
                                    "margin": "md",
                                    "contents": []
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