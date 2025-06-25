# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 23:15:05 2025

@author: lenovo
"""
import os
import json

# ==============================================================================
# 1. 配置区：定义所有需要生成的决策树
# ==============================================================================
# 将来添加新的决策树，只需要在此处添加一个新条目即可。
# 'key' 将作为文件名 (e.g., '2_1_poor_school_performance.json')
# 'title' 和 'description' 将显示在主页上。
TREES_CONFIG = {
    "2_1_poor_school_performance": {
        "title": "2.1 不良学校表现",
        "description": "评估与儿童或青少年学校表现不佳相关的潜在精神障碍。"
    },
    "2_2_behavioral_problems": {
        "title": "2.2 儿童或青少年中的行为问题",
        "description": "评估儿童或青少年中出现的各类行为问题的鉴别诊断。"
    },
    "2_3_language_disorders": {
        "title": "2.3 语言紊乱",
        "description": "对各种类型的语言紊乱进行鉴别诊断，包括其成因和表现。"
    },
    "2_4_distractibility": {
        "title": "2.4 随境转移",
        "description": "鉴别随境转移（分心）的各种可能原因。"
    },
    "2_5_delusions": {
        "title": "2.5 妄想",
        "description": "对不同类型的妄想及其相关精神障碍进行鉴别。"
    },
    "2_6_hallucinations": {
        "title": "2.6 幻觉",
        "description": "鉴别不同感官的幻觉体验及其潜在诊断。"
    },
    "2_7_catatonic_symptoms": {
        "title": "2.7 紧张症症状",
        "description": "评估和鉴别紧张症状态的病因。"
    },
    "2_8_elevated_or_expansive_mood": {
        "title": "2.8 高涨或膨胀的心境",
        "description": "鉴别躁狂、轻躁狂及相关心境状态。"
    },
    "2_9_irritable_mood": {
        "title": "2.9 易激惹心境",
        "description": "对易激惹心境的多种可能精神障碍进行区分。"
    },
    "2_10_depressed_mood": {
        "title": "2.10 抑郁心境",
        "description": "系统性地鉴别各种类型的抑郁障碍。"
    },
    "2_11_suicidal_ideation_or_behavior": {
        "title": "2.11 自杀观念或行为",
        "description": "评估与自杀观念或行为相关的精神状况。"
    },
    "2_12_psychomotor_retardation": {
        "title": "2.12 精神运动性迟滞",
        "description": "鉴别导致精神运动迟滞的各种原因。"
    },
    "2_13_anxiety": {
        "title": "2.13 焦虑",
        "description": "对广泛的焦虑症状进行系统性鉴别诊断。"
    },
    "2_14_panic_attacks": {
        "title": "2.14 惊恐发作",
        "description": "鉴别原发性与继发性惊恐发作。"
    },
    "2_15_avoidance": {
        "title": "2.15 回避行为",
        "description": "区分不同原因导致的回避行为。"
    },
    "2_16_trauma_and_stressors": {
        "title": "2.16 病因涉及创伤或心理社会应激源",
        "description": "鉴别与创伤和应激相关的障碍。"
    },
    "2_17_somatic_complaints": {
        "title": "2.17 躯体主诉或疾病/外貌焦虑",
        "description": "评估以躯体症状或健康焦虑为主要表现的障碍。"
    },
    "2_18_eating_or_appetite_changes": {
        "title": "2.18 食欲改变或异常的进食行为",
        "description": "对各类进食障碍及相关的行为模式进行鉴别。"
    },
    "2_19_insomnia": {
        "title": "2.19 失眠",
        "description": "鉴别不同原因导致的失眠问题。"
    },
    "2_20_hypersomnolence": {
        "title": "2.20 嗜睡",
        "description": "对日间过度思睡的各种病因进行区分。"
    },
    "2_21_sexual_dysfunction_in_a_female": {
        "title": "2.21 女性性功能失调",
        "description": "评估和鉴别女性性功能障碍。"
    },
    "2_22_sexual_dysfunction_in_a_male": {
        "title": "2.22 男性性功能失调",
        "description": "评估和鉴别男性性功能障碍。"
    },
    "2_23_aggressive_behavior": {
        "title": "2.23 攻击行为",
        "description": "对攻击行为的潜在精神病理原因进行鉴别。"
    },
    "2_24_impulsivity_or_impulse-control_problems": {
        "title": "2.24 冲动性或冲动控制问题",
        "description": "鉴别以冲动性为核心特征的多种障碍。"
    },
    "2_25_self-injury_or_self-mutilation": {
        "title": "2.25 自伤或自残",
        "description": "评估非自杀性自伤行为及相关障碍。"
    },
    "2_26_excessive_substance_use": {
        "title": "2.26 过度物质使用",
        "description": "对物质使用障碍及其相关精神症状进行鉴别。"
    },
    "2_27_memory_loss": {
        "title": "2.27 记忆丧失",
        "description": "鉴别不同类型的记忆障碍及其病因。"
    },
    "2_28_cognitive_impairment": {
        "title": "2.28 认知损害",
        "description": "对各种认知域的损害进行系统性评估。"
    },
    "2_29_somatic_conditions": {
        "title": "2.29 躯体疾病作为病因",
        "description": "评估由一般躯体疾病直接导致的各种精神症状。"
    }
}
# ==============================================================================
# 2. HTML 模板区 (决策树页面模板) - 经过验证的最终版
# ==============================================================================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{ --primary-color: #005A9C; --secondary-color: #6c757d; --success-color: #198754; --danger-color: #dc3545; --info-color: #0dcaf0;
            --light-bg: #f0f2f5; --border-color: #d9d9d9; --text-color: #333; --white-color: #ffffff;
        }}
        body {{
            font-family: "PingFang SC", "Helvetica Neue", Helvetica, Arial, "Microsoft Yahei", sans-serif;
            background-color: var(--light-bg); color: var(--text-color); margin: 0; padding: 2rem;
            display: flex; justify-content: center;
        }}
        .main-container {{
            width: 100%; max-width: 900px; background-color: var(--white-color);
            border: 1px solid var(--border-color); border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }}
        header {{
             background-color: var(--primary-color); color: var(--white-color); padding: 1.5rem 2rem;
             border-top-left-radius: 8px; border-top-right-radius: 8px;
        }}
        header h1 {{ font-size: 1.75rem; margin: 0; }}
        .content-wrapper {{ padding: 2rem; }}
        .history-container {{ margin-bottom: 2rem; }}
        .history-container h2 {{
            font-size: 1.1rem; color: var(--secondary-color); border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem; margin-bottom: 1rem;
        }}
        #history-log {{
            list-style-type: none; padding-left: 0; margin: 0;
            font-size: 0.95rem; max-height: 300px; overflow-y: auto;
        }}
        .log-item {{
            display: flex; align-items: flex-start; margin-bottom: 1rem;
        }}
        .step-number {{
            font-weight: bold; color: var(--primary-color); background-color: #e6f7ff; border-radius: 50%;
            width: 24px; height: 24px; min-width: 24px;
            display: inline-flex; align-items: center; justify-content: center; margin-right: 12px;
        }}
        .log-content {{ flex-grow: 1; }}
        .question-text {{ color: #333; display: block; }}
        .choice-section {{
            margin-top: 0.5rem; display: flex; align-items: center; flex-wrap: wrap;
        }}
        .choice-text {{
            font-weight: bold; padding: 2px 8px; border-radius: 4px; color: white;
        }}
        .choice-yes {{ background-color: var(--success-color); }}
        .choice-no {{ background-color: var(--danger-color); }}
        .remark-text {{
            margin-left: 10px; padding: 4px 8px; background-color: #eee;
            border-radius: 4px; font-style: italic; color: #555;
            border-left: 3px solid var(--secondary-color);
        }}
        .log-connector {{
            width: 100%; text-align: center; color: var(--border-color);
            font-size: 1.5rem; line-height: 0.5; margin-bottom: 0.5rem;
        }}
        .final-result-log {{
            background-color: #e6f7ff; border: 1px solid #91d5ff; padding: 1rem;
            border-radius: 4px; font-weight: bold; color: var(--primary-color);
            margin-top: -1rem;
        }}
        .flowchart-step fieldset {{
            border: 2px solid var(--primary-color); border-radius: 6px; padding: 1.5rem; background-color: #f8f9fa;
        }}
        .flowchart-step legend {{
            font-weight: bold; padding: 0 0.5em; font-size: 1.1rem; color: var(--primary-color);
        }}
        #node-display {{
            font-size: 1.3rem; line-height: 1.6; min-height: 100px; display: flex;
            align-items: center; justify-content: center; text-align: center; margin-bottom: 1rem;
        }}
        .remark-input-container {{ margin-bottom: 1.5rem; text-align: center; }}
        #remark-input {{
            width: 80%; padding: 8px 12px; border: 1px solid var(--border-color);
            border-radius: 4px; font-size: 0.95rem;
        }}
        #remark-input:focus {{
            outline: none; border-color: var(--primary-color); box-shadow: 0 0 0 2px rgba(0, 90, 156, 0.2);
        }}
        .controls {{ display: flex; justify-content: space-between; }}
        .controls button, .footer-controls button {{
            font-size: 1rem; padding: 0.75rem 0; border-radius: 5px; border: 1px solid;
            cursor: pointer; transition: all 0.2s ease-in-out; font-weight: 500; width: 48%;
        }}
        #yes-btn {{ background-color: var(--success-color); color: var(--white-color); border-color: var(--success-color); }}
        #no-btn {{ background-color: var(--danger-color); color: var(--white-color); border-color: var(--danger-color);}}
        #yes-btn:hover {{ background-color: #157347; border-color: #146c43; }}
        #no-btn:hover {{ background-color: #bb2d3b; border-color: #b02a37; }}
        .footer-controls {{
            margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--border-color);
            display: flex; justify-content: space-between; align-items: center;
        }}
        .footer-controls .btn-group {{ display: flex; gap: 1rem; flex-wrap: wrap; }}
        .footer-controls button {{ width: auto; padding: 0.5rem 1.2rem; }}
        #back-btn, #restart-btn {{ background-color: var(--white-color); color: var(--secondary-color); border-color: var(--secondary-color); }}
        #export-btn {{ background-color: var(--white-color); color: var(--info-color); border-color: var(--info-color); }}
        #back-btn:hover, #restart-btn:hover {{ background-color: #e9ecef; }}
        #export-btn:hover {{ background-color: #cff4fc; }}
        #back-btn:disabled, #export-btn:disabled {{ background-color: #e9ecef; cursor: not-allowed; opacity: 0.7; border-color: var(--border-color); color: var(--secondary-color); }}
        .footer-controls a {{ color: var(--primary-color); text-decoration: none; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <div class="main-container">
        <header><h1>{title}</h1></header>
        <div class="content-wrapper">
            <div class="history-container">
                <h2>诊断路径</h2>
                <ul id="history-log"><li>开始诊断...</li></ul>
            </div>
            <div id="flowchart-container">
                <div class="flowchart-step">
                    <fieldset>
                        <legend>当前步骤</legend>
                        <div id="node-display"></div>
                        <div id="remark-container" class="remark-input-container">
                            <input type="text" id="remark-input" placeholder="添加备注 (可选)">
                        </div>
                        <div id="controls" class="controls">
                            <button id="no-btn">否 (No)</button>
                            <button id="yes-btn">是 (Yes)</button>
                        </div>
                    </fieldset>
                </div>
            </div>
            <div class="footer-controls">
                <div class="btn-group">
                    <button id="back-btn">上一步</button>
                    <button id="restart-btn">重新开始</button>
                    <button id="export-btn">导出诊断报告</button>
                </div>
                <a href="index.html">返回主索引</a>
            </div>
        </div>
    </div>
    <script>
        const treeData = {tree_data_json};
        const pageTitle = "{title}";
        const startNodeId = 'start';
        let currentNode;
        let history = [];
        const nodeDisplay = document.getElementById('node-display');
        const flowchartContainer = document.getElementById('flowchart-container');
        const controlsDiv = document.getElementById('controls');
        const remarkContainer = document.getElementById('remark-container');
        const remarkInput = document.getElementById('remark-input');
        const yesBtn = document.getElementById('yes-btn');
        const noBtn = document.getElementById('no-btn');
        const backBtn = document.getElementById('back-btn');
        const restartBtn = document.getElementById('restart-btn');
        const exportBtn = document.getElementById('export-btn');
        const historyLog = document.getElementById('history-log');
        function findNodeById(id) {{ return treeData.find(node => node.id === id); }}
        function buildHistoryTree(path, finalNode) {{
            if (path.length === 0 && !finalNode) {{ return '<li>开始诊断...</li>'; }}
            let html = '';
            path.forEach((step, index) => {{
                const node = findNodeById(step.nodeId);
                const choiceText = step.choice === 'yes' ? '是' : '否';
                const choiceClass = step.choice === 'yes' ? 'choice-yes' : 'choice-no';
                html += `<li class="log-item"><div class="step-number">${{index + 1}}</div><div class="log-content"><div class="question-text">"${{node.text}}"</div><div class="choice-section"><span class="choice-text ${{choiceClass}}">${{choiceText}}</span>`;
                if (step.remark) {{ html += `<div class="remark-text">${{step.remark}}</div>`; }}
                html += `</div></div></li><div class="log-connector">↓</div>`;
            }});
            if (finalNode && finalNode.type === 'result') {{ html += `<div class="final-result-log">${{finalNode.text}}</div>`; }}
            return html;
        }}
        function updateHistoryDisplay() {{
            historyLog.innerHTML = buildHistoryTree(history, currentNode);
            historyLog.scrollTop = historyLog.scrollHeight;
        }}
        function updateButtonStates() {{
            backBtn.disabled = history.length === 0;
            exportBtn.disabled = history.length === 0 || !currentNode || currentNode.type !== 'result';
        }}
        function showNode(nodeId) {{
            currentNode = findNodeById(nodeId);
            if (!currentNode) {{
                nodeDisplay.textContent = '错误：未找到节点 ' + nodeId;
                flowchartContainer.style.display = 'none';
                return;
            }}
            updateHistoryDisplay();
            updateButtonStates();
            if (currentNode.type === 'question') {{
                nodeDisplay.textContent = currentNode.text;
                flowchartContainer.style.display = 'block';
            }} else {{
                flowchartContainer.style.display = 'none';
            }}
        }}
        function makeChoice(isYes) {{
            if (!currentNode) return;
            const choice = isYes ? 'yes' : 'no';
            const remark = remarkInput.value.trim();
            history.push({{ nodeId: currentNode.id, choice: choice, remark: remark }});
            remarkInput.value = '';
            const nextNodeId = isYes ? currentNode.yes_target : currentNode.no_target;
            showNode(nextNodeId);
        }}
        function generateReportText() {{
            let report = `DSM-5® 鉴别诊断报告\\n====================================\\n`;
            report += `决策树: ${{pageTitle}}\\n生成时间: ${{new Date().toLocaleString('zh-CN')}}\\n====================================\\n\\n`;
            history.forEach((step, index) => {{
                const node = findNodeById(step.nodeId);
                const choiceText = step.choice === 'yes' ? '是' : '否';
                report += `步骤 ${{index + 1}}: \\n  - 问题: ${{node.text}}\\n  - 选择: ${{choiceText}}\\n`;
                if (step.remark) {{ report += `  - 备注: ${{step.remark}}\\n`; }}
                report += `\\n`;
            }});
            if (currentNode && currentNode.type === 'result') {{ report += `最终诊断/结论:\\n  - ${{currentNode.text}}\\n`; }}
            return report;
        }}
        function exportReport() {{
            if (exportBtn.disabled) return;
            const reportText = generateReportText();
            const blob = new Blob([reportText], {{ type: 'text/plain;charset=utf-8' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
            a.download = `DSM5_Report_${{timestamp}}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}
        yesBtn.addEventListener('click', () => makeChoice(true));
        noBtn.addEventListener('click', () => makeChoice(false));
        exportBtn.addEventListener('click', exportReport);
        backBtn.addEventListener('click', () => {{
            if (history.length > 0) {{
                const lastStep = history.pop();
                showNode(lastStep.nodeId);
                remarkInput.value = lastStep.remark || '';
            }}
        }});
        restartBtn.addEventListener('click', () => {{
            history = [];
            remarkInput.value = '';
            showNode(startNodeId);
        }});
        showNode(startNodeId);
    </script>
</body>
</html>
"""

# ==============================================================================
# 3. 主生成逻辑
# ==============================================================================
def generate_pages():
    output_dir = "dsm5_handbook_web"
    data_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.isdir(data_dir):
        print(f"错误: 'data' 文件夹未找到。请创建 '{data_dir}' 文件夹并放入JSON数据文件。")
        return

    print(f"文件将生成在 '{output_dir}' 文件夹中...")

    # --- 动态生成决策树页面 ---
    for key, details in TREES_CONFIG.items():
        filename_base = key
        json_path = os.path.join(data_dir, f"{filename_base}.json")

        if not os.path.exists(json_path):
            print(f"  - 警告: 未找到 {json_path}，跳过生成 {filename_base}.html")
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                tree_data = json.load(f)
            tree_data_json_string = json.dumps(tree_data, ensure_ascii=False)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"  - 错误: 读取或解析 {json_path} 失败: {e}，跳过此文件。")
            continue
        
        filepath = os.path.join(output_dir, f"{filename_base}.html")
        
        # 使用 .format() 方法，确保占位符是正确的单大括号
        content = HTML_TEMPLATE.format(title=details["title"], tree_data_json=tree_data_json_string)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  - 已生成: {filename_base}.html")

    # --- 生成主索引页面 (简洁专业版) ---
    index_path = os.path.join(output_dir, "index.html")
    index_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DSM-5® 鉴别诊断手册 - 决策树索引</title>
        <style>
            :root {{
                --primary-color: #005A9C; --primary-dark: #004071; --light-bg: #f8f9fa;
                --card-bg: #ffffff; --text-color: #212529; --text-secondary: #6c757d;
                --border-color: #dee2e6;
            }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
                background-color: var(--light-bg); color: var(--text-color); margin: 0;
            }}
            .main-wrapper {{
                width: 100%; display: flex; justify-content: center;
                padding: 4rem 1rem; box-sizing: border-box;
            }}
            .container {{ width: 100%; max-width: 1100px; }}
            .header {{
                text-align: left; margin-bottom: 2.5rem; border-bottom: 1px solid var(--border-color);
                padding-bottom: 1.5rem;
            }}
            .header h1 {{
                font-size: 2rem; margin: 0 0 0.25rem 0; font-weight: 600; color: var(--primary-dark);
            }}
            .header p {{ font-size: 1.1rem; margin: 0; color: var(--text-secondary); }}
            .card-list {{ display: flex; flex-direction: column; gap: 1rem; }}
            .card {{
                background: var(--card-bg); border: 1px solid var(--border-color);
                border-radius: 8px; transition: border-color 0.2s ease, box-shadow 0.2s ease;
                display: block;
            }}
            .card.disabled {{ background-color: #fcfcfc; opacity: 0.6; }}
            .card:not(.disabled) {{ cursor: pointer; }}
            .card:not(.disabled):hover {{
                border-color: var(--primary-color); box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
            }}
            .card a {{
                text-decoration: none; color: inherit; display: block; padding: 1.5rem;
            }}
            .card.disabled a {{ pointer-events: none; }}
            .item-title {{
                font-size: 1.1rem; font-weight: 500; color: var(--text-color);
                margin: 0 0 0.5rem 0;
            }}
            .item-desc {{
                font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6; margin: 0;
            }}
            @media (max-width: 600px) {{
                .main-wrapper {{ padding: 2rem 1rem; }}
                .header h1 {{ font-size: 1.5rem; }}
                .header p {{ font-size: 1rem; }}
                .card a {{ padding: 1.25rem; }}
            }}
        </style>
    </head>
    <body>
        <div class="main-wrapper">
            <div class="container">
                <header class="header">
                    <h1>DSM-5® 交互式鉴别诊断</h1>
                    <p>基于《鉴别诊断手册》第二章：用树形图做鉴别诊断</p>
                </header>
                <div class="card-list">
    """
    for key, details in TREES_CONFIG.items():
        json_path = os.path.join(data_dir, f"{key}.json")
        is_disabled = not os.path.exists(json_path)
        card_class = "card disabled" if is_disabled else "card"
        href = f"{key}.html" if not is_disabled else "javascript:void(0);"
        
        index_content += f"""
                    <div class="{card_class}">
                        <a href="{href}">
                            <h3 class="item-title">{details["title"]}</h3>
                            <p class="item-desc">{details["description"]}</p>
                        </a>
                    </div>"""
    
    index_content += """
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"  - 已生成最终版: index.html")
    print("\n生成完成！")

if __name__ == "__main__":
    generate_pages()
