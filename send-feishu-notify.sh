#!/bin/bash
# 发送飞书群消息通知
# 用法：send-feishu-notify.sh "消息内容" "成功/失败"

MESSAGE="$1"
STATUS="$2"
CHAT_ID="oc_38ec57abca24e1caf76e3bb8e9b4261d"

# 根据状态设置颜色和图标
if [ "$STATUS" = "成功" ]; then
    COLOR="green"
    ICON="🌸"
else
    COLOR="red"
    ICON="⚠️"
fi

# 创建消息内容（飞书卡片格式）
cat <<EOF
{
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": true
        },
        "header": {
            "template": "${COLOR}",
            "title": {
                "content": "${ICON} 记忆看板更新${STATUS}",
                "tag": "plain_text"
            }
        },
        "elements": [
            {
                "tag": "markdown",
                "content": "${MESSAGE}"
            },
            {
                "tag": "note",
                "elements": [
                    {
                        "tag": "plain_text",
                        "content": "更新时间：$(date '+%Y-%m-%d %H:%M:%S')"
                    }
                ]
            }
        ]
    }
}
EOF
