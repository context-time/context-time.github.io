# -*- coding: utf-8 -*-
"""Refresh asset versions and generate the standalone Chinese tutorial page.

Edit dist/index.html and the translations below, then run this script.
Speakers and schedule have bilingual data in dist/content.js.
"""
from pathlib import Path
import hashlib
import re

root = Path(__file__).resolve().parents[1] / 'dist'
source = (root / 'index.html').read_text()
for asset in ['style.css', 'content.js', 'app.js']:
    version = hashlib.sha256((root / asset).read_bytes()).hexdigest()[:10]
    source = re.sub(r'(?P<attr>href|src)="' + re.escape(asset) + r'(?:\?v=[^"]*)?"', lambda match: match.group('attr') + '="' + asset + '?v=' + version + '"', source)
(root / 'index.html').write_text(source)
translations = {
    '<html lang="en">': '<html lang="zh-CN">',
    'Tutorial overview, case study, and references for the ICDM 2026 tutorial on context-aware time series forecasting with LLMs.': 'ICDM 2026 教程「大模型驱动的情境感知时间序列预测」的简介、案例和参考文献。',
    '>Context-Aware Time Series Forecasting with LLMs: From Pattern Recognition to Cognitive Reasoning</h1>': '><span>大模型驱动的</span><span>情境感知</span><span>时间序列预测：</span><span>从模式识别到认知推理</span></h1>',
    'Context-Aware Time Series Forecasting with LLMs: From Pattern Recognition to Cognitive Reasoning': '大模型驱动的情境感知时间序列预测：从模式识别到认知推理',
    'November 15, 2026, Shenyang, China.': '2026 年 11 月 15 日，中国沈阳。',
    'ICDM 2026 Tutorial': 'ICDM 2026 教程',
    'Skip to content': '跳至正文',
    'Main navigation': '主导航',
    'Page language': '页面语言',
    'November 15, 2026': '2026 年 11 月 15 日',
    '>Wanda Vista Shenyang<': '>沈阳富力万达文华酒店<',
    '>News<': '>动态<',
    'The tutorial slides will be publicly available on this page soon.': '本教程的幻灯片即将在此页面公开。',
    (
        'This tutorial explores advances in context-aware time series forecasting with large language models, moving beyond '
        'historical pattern recognition toward context-grounded cognitive reasoning. Real-world forecasts depend on temporal '
        'patterns, external conditions, events, domain knowledge, and system states. Using context as <strong>predictive evidence</strong> '
        'starts with evaluating what additional features tell us. <strong>What evidence matters, what evidence can we trust, and how can we '
        'verify its influence on the future?</strong> The tutorial approaches this question through multimodal semantic '
        'understanding, slow-thinking reasoning over evidence, and agentic interaction with tools and environments. It '
        'discusses applications in electricity load, renewable power, traffic, industry, and scientific forecasting, and '
        'highlights open challenges and future directions.'
    ): (
        '本教程介绍大模型驱动的情境感知时间序列预测的研究进展，探讨如何从历史模式识别走向基于情境的认知推理。现实中的预测受到时间规'
        '律、外部条件、事件、领域知识和系统状态的共同影响。要把附加特征用作<strong>预测证据</strong>，需要先判断它们能说明什么。'
        '<strong>哪些证据与预测有关，哪些证据值得信赖，又该怎样验证它们对未来的影响？</strong>教程从多模态语义理'
        '解、基于证据的慢思考推理，以及智能体与工具和环境的交互三个方面展开，讨论电力负荷、可再生能源发电、交通、工业和科学预测中的'
        '应用，以及尚待解决的挑战与研究方向。'
    ),
    '>Overview<': '>简介<',
    '>Same History, Different Futures<': '>相同历史，不同未来<',
    'src="assets/same-history-different-futures.png" width="1200" height="790"': 'src="assets/same-history-different-futures-zh.png" width="1545" height="1018"',
    'href="assets/same-history-different-futures.png"': 'href="assets/same-history-different-futures-zh.png"',
    '>View full-size figure<': '>查看原图<',
    '>Read the case as text<': '>阅读中文版案例说明<',
    (
        'Consider tomorrow’s electricity demand in one region. Both scenarios start from identical historical '
        'observations and assume the same weekday conditions. Under normal weather, electricity demand may follow '
        'a familiar daily pattern. During a heatwave, increased cooling demand can raise and prolong the afternoon peak.'
    ): (
        '以同一地区的次日用电需求为例，两种情境采用同一段历史观测，并假设次日均为普通工作日。天气正常时，'
        '用电负荷可能延续常见的日内变化规律。热浪期间，制冷用电增加，下午的负荷峰值可能升高，高负荷时段也可能延长。'
    ),
    '>Scenario A — Normal Weekday<': '>情境 A · 正常天气下的工作日<',
    '>Scenario B — Heatwave Weekday<': '>情境 B · 热浪下的工作日<',
    '<strong>27°C</strong> maximum temperature': '最高气温 <strong>27°C</strong>',
    '<strong>37°C</strong> maximum temperature': '最高气温 <strong>37°C</strong>',
    'Normal cooling demand and a familiar daily load pattern.': '制冷需求正常，负荷延续常见的日内变化规律。',
    'Increased cooling demand and a higher, potentially longer afternoon peak.': '制冷需求增加，下午峰值更高，高负荷时段也可能延长。',
    (
        'Synthetic electricity demand forecasts share the same history, region, and weekday. '
        'The orange 37°C heatwave curve reaches a higher afternoon peak than the blue 27°C normal weekday curve. '
        'The figure asks which evidence matters, how it shapes the forecast, and whether the forecast is plausible.'
    ): '图中用合成数据展示同一地区和工作日条件下，从同一段历史负荷出发的两条预测。37°C 热浪情境的橙色曲线比 27°C 正常天气情境的蓝色曲线有更高的下午峰值。图末提出三个问题：哪些证据重要、它们如何影响预测，以及预测结果是否合理。',
    'Illustrative forecasts based on synthetic data.': '预测曲线基于合成数据，仅用于示意。',
    '>EIA analysis of cooling demand during a heatwave<': '>EIA 对热浪期间制冷用电的分析<',
    '>Three Key Questions<': '>三个关键问题<',
    (
        'The forecasting challenge is to identify relevant evidence, explain how it changes the load curve, '
        'and verify that the predicted response is reasonable.'
    ): '预测的难点在于识别相关证据，解释它如何影响负荷曲线，并验证预测结果是否合理。',
    '>Evidence — What matters?<': '>证据 · 什么信息重要？<',
    'Which external information is relevant and trustworthy for forecasting?': '哪些外部信息与预测相关，且值得信赖？',
    '>Reasoning — Why and how?<': '>推理 · 影响从何而来？<',
    'How does contextual evidence influence the direction, magnitude, and timing of future changes?': '情境证据如何影响未来变化的方向、幅度和时间？',
    '>Verification — Can we trust it?<': '>验证 · 预测能否信赖？<',
    'Does the predicted response agree with the available evidence and known system constraints?': '预测结果是否符合现有证据和已知的系统约束？',
    '>Homepage<': '>首页<',
    '>Tutorial Organizers<': '>教程组织者<',
    '>Organizers<': '>组织者<',
    '>Tutorial Outline<': '>教程提纲<',
    '>Outline<': '>提纲<',
    '>References<': '>参考文献<',
    'Add to calendar': '添加到日历',
    'assets/tutorial.ics': 'assets/tutorial-zh.ics',
    '>Conference<': '>会议官网<',
    '>Contact<': '>联系团队<',
    'ICDM 2026 · Shenyang': 'ICDM 2026 · 沈阳',
}
chinese = source
for original, translated in sorted(translations.items(), key=lambda pair: len(pair[0]), reverse=True):
    if original not in chinese:
        raise ValueError(f'Translation source missing: {original[:90]}')
    chinese = chinese.replace(original, translated)
chinese = chinese.replace('hreflang="zh-CN" aria-label="切换到中文"', 'hreflang="zh-CN" aria-current="page" aria-label="中文版"')
chinese = chinese.replace('hreflang="en" aria-current="page" aria-label="English version"', 'hreflang="en" aria-label="Switch to English"')
(root / 'zh.html').write_text(chinese)
print('Updated asset versions and generated dist/zh.html.')
