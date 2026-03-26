content = open('index.html', 'r', encoding='utf-8').read()
insert_point = content.find('<!-- 报告卡片 3 - 新能源 -->')

new_cards = """            <!-- 报告卡片 5 - 笔记本电脑 -->
            <div class="report-card featured" data-category="科技">
                <div class="card-image">💻</div>
                <div class="category">💻 科技/PC</div>
                <div class="content">
                    <h3>笔记本电脑行业分析报告 2026 <span class="badge badge-new">NEW</span></h3>
                    <p>出货量 -10.4%、均价 +17-40%、AI PC 渗透延迟，深度分析 PC 产业格局与购买建议...</p>
                    <div class="tags">
                        <span class="tag">笔记本</span>
                        <span class="tag">联想</span>
                        <span class="tag">AI PC</span>
                    </div>
                    <div class="meta">
                        <span class="date">📅 2026-03-26</span>
                        <div class="stats">
                            <span class="stat">👁️ 最新发布</span>
                        </div>
                    </div>
                </div>
                <a href="reports/笔记本电脑行业分析报告%202026.html" class="btn">📖 阅读全文</a>
            </div>

            <!-- 报告卡片 6 - AI 大模型 -->
            <div class="report-card featured" data-category="人工智能">
                <div class="card-image">🤖</div>
                <div class="category">🤖 人工智能/大模型</div>
                <div class="content">
                    <h3>AI 大模型行业分析报告 2026 <span class="badge badge-new">NEW</span></h3>
                    <p>全球$77-150 亿市场、中国 Token 份额 30%、Claude Code 6 个月$1B run rate，深度分析 LLM 产业格局...</p>
                    <div class="tags">
                        <span class="tag">LLM</span>
                        <span class="tag">OpenAI</span>
                        <span class="tag">月之暗面</span>
                    </div>
                    <div class="meta">
                        <span class="date">📅 2026-03-26</span>
                        <div class="stats">
                            <span class="stat">👁️ 最新发布</span>
                        </div>
                    </div>
                </div>
                <a href="reports/AI%20大模型行业分析报告%202026.html" class="btn">📖 阅读全文</a>
            </div>

            <!-- 报告卡片 7 - 全球经济 -->
            <div class="report-card featured" data-category="全球经济">
                <div class="card-image">🌍</div>
                <div class="category">🌍 全球经济/行业分析</div>
                <div class="content">
                    <h3>全球主流行业经济情况报告 2026 <span class="badge badge-new">NEW</span></h3>
                    <p>全球 GDP 2.8-3.3% 增速、AI 行业 50-60% 领跑、12 个主流行业深度对比，全景扫描全球经济...</p>
                    <div class="tags">
                        <span class="tag">全球经济</span>
                        <span class="tag">GDP</span>
                        <span class="tag">行业对比</span>
                    </div>
                    <div class="meta">
                        <span class="date">📅 2026-03-26</span>
                        <div class="stats">
                            <span class="stat">👁️ 最新发布</span>
                        </div>
                    </div>
                </div>
                <a href="reports/全球主流行业经济情况报告%202026.html" class="btn">📖 阅读全文</a>
            </div>

            <!-- 报告卡片 8 - 可再生能源 -->
            <div class="report-card featured" data-category="能源">
                <div class="card-image">⚡</div>
                <div class="category">⚡ 能源/可再生能源</div>
                <div class="content">
                    <h3>可再生能源行业分析报告 2026 <span class="badge badge-new">NEW</span></h3>
                    <p>储能 +56.7%、AI 用电 80GW→150GW、中国风光 18.4 亿千瓦，深度分析能源转型与投资机遇...</p>
                    <div class="tags">
                        <span class="tag">太阳能</span>
                        <span class="tag">风能</span>
                        <span class="tag">储能</span>
                    </div>
                    <div class="meta">
                        <span class="date">📅 2026-03-26</span>
                        <div class="stats">
                            <span class="stat">👁️ 最新发布</span>
                        </div>
                    </div>
                </div>
                <a href="reports/可再生能源行业分析报告%202026.html" class="btn">📖 阅读全文</a>
            </div>

            <!-- 报告卡片 9 - AI 玩具 -->
            <div class="report-card featured" data-category="消费">
                <div class="card-image">🧸</div>
                <div class="category">🧸 消费/AI 玩具</div>
                <div class="content">
                    <h3>AI 玩具行业分析报告 2026 <span class="badge badge-new">NEW</span></h3>
                    <p>中国 290 亿市场、线上 +394.9%、2030 年破千亿，深度分析智能玩具与陪伴机器人产业...</p>
                    <div class="tags">
                        <span class="tag">AI 玩具</span>
                        <span class="tag">陪伴机器人</span>
                        <span class="tag">美泰</span>
                    </div>
                    <div class="meta">
                        <span class="date">📅 2026-03-26</span>
                        <div class="stats">
                            <span class="stat">👁️ 最新发布</span>
                        </div>
                    </div>
                </div>
                <a href="reports/AI%20玩具行业分析报告%202026.html" class="btn">📖 阅读全文</a>
            </div>

            <!-- 报告卡片 10 - AI 教育 -->
            <div class="report-card featured" data-category="教育">
                <div class="card-image">📚</div>
                <div class="category">📚 教育/EdTech</div>
                <div class="content">
                    <h3>AI 教育行业分析报告 2026 <span class="badge badge-new">NEW</span></h3>
                    <p>全球$95.8 亿市场、学生 AI 使用率 92%、学习效果 +54%，深度分析 AI+ 教育融合与投资机遇...</p>
                    <div class="tags">
                        <span class="tag">AI 教育</span>
                        <span class="tag">EdTech</span>
                        <span class="tag">个性化学习</span>
                    </div>
                    <div class="meta">
                        <span class="date">📅 2026-03-26</span>
                        <div class="stats">
                            <span class="stat">👁️ 最新发布</span>
                        </div>
                    </div>
                </div>
                <a href="reports/AI%20教育行业分析报告%202026.html" class="btn">📖 阅读全文</a>
            </div>

"""

new_content = content[:insert_point] + new_cards + content[insert_point:]
open('index.html', 'w', encoding='utf-8').write(new_content)
print('Homepage updated successfully!')
