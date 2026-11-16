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
    'Tutorial overview, practical takeaways, and references for the ICDM 2026 tutorial on context-aware time series forecasting with LLMs.': 'ICDM 2026 教程「大模型驱动的情境感知时间序列预测」的简介、实践要点和参考文献。',
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
    'Forecasting tomorrow’s electricity demand': '预测次日用电需求',
    'A grid operator forecasts tomorrow’s electricity demand for the same region under two scenarios. Both forecasts start from the same observed demand.': '电网调度员要预测同一地区次日的用电需求。两种情境都以同一段历史负荷为起点。',
    'Three forecasts start from the same observed electricity demand. Demand rises on a hot workday, stays roughly flat in the history-only forecast, and falls on a mild-weather holiday.': '三条预测曲线基于同一段历史电力负荷。高温工作日的预测负荷上升，仅依据历史的预测基本持平，天气温和的假日预测负荷下降。',
    '>Past demand<': '>历史负荷<',
    '>Tomorrow’s forecast<': '>次日预测<',
    '>Electricity demand<': '>电力负荷<',
    '<strong>Hot workday:</strong> higher demand as cooling use rises.': '<strong>高温工作日：</strong>制冷用电增加，预测负荷上升。',
    '<strong>History only:</strong> roughly flat in this example.': '<strong>仅用历史数据：</strong>本例中预测负荷基本持平。',
    '<strong>Mild holiday:</strong> lower demand as businesses use less electricity.': '<strong>天气温和的假日：</strong>商业用电减少，预测负荷下降。',
    'Illustrative forecasts with synthetic data.': '曲线为合成数据示意。',
    '>Homepage<': '>首页<',
    '>Takeaways<': '>要点<',
    'How can LLMs use context for forecasting?': '大模型如何利用情境信息进行预测？',
    'Context-aware forecasting involves three connected capabilities: integrating contextual information, reasoning with predictive evidence, and adaptively acquiring additional context when needed.': '情境感知预测涉及三项相互关联的能力：整合情境信息、依据预测证据进行推理，以及在需要时自适应地获取更多情境信息。',
    'How can we integrate context?': '如何整合情境信息？',
    '>Multimodal Context Integration<': '>多模态情境整合<',
    (
        'Connect historical observations with external information, such as weather forecasts, event reports, calendars, '
        'and domain knowledge. The challenge is to understand heterogeneous context, align it with the prediction target '
        'and horizon, and combine it with temporal patterns—not simply append more inputs.'
    ): (
        '将历史观测与天气预报、事件报道、日历和领域知识等外部信息联系起来。整合的关键在于理解不同来源和形式的情境信息，'
        '将它们与预测目标和预测时段对齐，再结合时间序列的变化规律进行建模。'
    ),
    'How can we reason with contextual evidence?': '如何依据情境证据进行推理？',
    '>Evidence-Grounded Reasoning<': '>基于证据的推理<',
    (
        'Identify predictive evidence within the available context and reason about how it may shape future dynamics. '
        'This involves assessing the direction, magnitude, and timing of potential effects, weighing competing evidence, '
        'and revising forecast hypotheses while accounting for uncertainty.'
    ): (
        '从可用的情境信息中识别与预测有关的证据，推断它们可能怎样影响未来走势。具体来说，需要判断潜在影响的方向、幅度和时间，'
        '权衡指向不同结论的证据，并在考虑不确定性的同时修正预测假设。'
    ),
    'How can we acquire context adaptively?': '如何自适应地获取情境信息？',
    '>Adaptive Context Acquisition<': '>自适应情境获取<',
    (
        'Determine whether the available evidence is sufficient and what additional information could resolve uncertainty. '
        'A forecasting agent can selectively retrieve information, call tools, or request input, then update its reasoning '
        'and forecast. Acquisition should respect forecast-time availability and stop when further information is unlikely '
        'to justify its cost.'
    ): (
        '判断已有证据是否充分，以及哪些补充信息可以减少不确定性。预测智能体可以按需检索资料、调用工具或向用户询问，'
        '再更新推理和预测。获取的信息应在作出预测时可得。当继续搜集信息的预期收益不足以抵偿成本时，就应停止。'
    ),
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
