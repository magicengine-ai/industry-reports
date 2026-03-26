content = open('index.html', 'r', encoding='utf-8').read()

# 找到 AI 教育卡片后的位置
insert_marker = '<!-- 报告卡片 10 - AI 教育 -->'
insert_point = content.find(insert_marker)

if insert_point > 0:
    # 找到 AI 教育卡片的结束
    search_start = insert_point
    for _ in range(10):  # 找 10 个</div>
        end_point = content.find('</div>', search_start)
        search_start = end_point + 6
    
    new_card = """

            <!-- 报告卡片 11 - LED 屏幕 -->
            <div class="report-card featured" data-category="科技">
                <div class="card-image">📺</div>
                <div class="category">📺 科技/显示</div>
                <div class="content">
                    <h3>LED 屏幕行业分析报告 2026 <span class="badge badge-new">NEW</span></h3>
                    <p>全球$121.76 亿市场、Mini LED +20%、Micro LED +100%、海信垄断 90%，深度分析显示技术与商业应用...</p>
                    <div class="tags">
                        <span class="tag">Mini LED</span>
                        <span class="tag">Micro LED</span>
                        <span class="tag">小间距 LED</span>
                    </div>
                    <div class="meta">
                        <span class="date">📅 2026-03-26</span>
                        <div class="stats">
                            <span class="stat">👁️ 最新发布</span>
                        </div>
                    </div>
                </div>
                <a href="reports/LED%20屏幕行业分析报告%202026.html" class="btn">📖 阅读全文</a>
            </div>
"""
    
    new_content = content[:end_point] + new_card + content[end_point:]
    open('index.html', 'w', encoding='utf-8').write(new_content)
    print('LED display report card added to homepage!')
else:
    print('Insert point not found!')
