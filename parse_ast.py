import re
from collections import defaultdict

def parse_ast(ast_content):
    # 用于存储节点信息和节点之间的关系
    nodes = {}
    edges = defaultdict(list)

    # 使用正则表达式来提取节点和边
    node_pattern = re.compile(r'\"(\d+)\"\s+\[label\s*=\s*<(.+?)>\s*\]')
    edge_pattern = re.compile(r'\"(\d+)\"\s+->\s+\"(\d+)\"')
    sub_pattern = re.compile(r'<SUB>.*?<\/SUB>')

    # 提取所有节点
    for node in node_pattern.findall(ast_content):
        node_id, label = node
        # Remove the "<SUB>...</SUB>" part
        label = sub_pattern.sub('', label)
        # 清理标签并存储
        clean_label = re.sub(r'<|>', '', label).replace('&lt;', '<').replace('&amp;', '&').replace('&gt;', '>')
        nodes[node_id] = clean_label

    # 提取所有边
    for edge in edge_pattern.findall(ast_content):
        source, target = edge
        edges[source].append(target)

    return nodes, edges

# 示例AST内容
ast_content = """

"7" [label = <(METHOD,max)<SUB>4</SUB>> ]
"8" [label = <(PARAM,int a)<SUB>4</SUB>> ]
"9" [label = <(PARAM,int b)<SUB>4</SUB>> ]
"10" [label = <(BLOCK,&lt;empty&gt;,&lt;empty&gt;)<SUB>4</SUB>> ]
"11" [label = <(RETURN,return a&gt;b?a:b;,return a&gt;b?a:b;)<SUB>5</SUB>> ]
"12" [label = <(&lt;operator&gt;.conditional,a&gt;b?a:b)<SUB>5</SUB>> ]
"13" [label = <(&lt;operator&gt;.greaterThan,a&gt;b)<SUB>5</SUB>> ]
"14" [label = <(IDENTIFIER,a,a&gt;b)<SUB>5</SUB>> ]
"15" [label = <(IDENTIFIER,b,a&gt;b)<SUB>5</SUB>> ]
"16" [label = <(IDENTIFIER,a,a&gt;b?a:b)<SUB>5</SUB>> ]
"17" [label = <(IDENTIFIER,b,a&gt;b?a:b)<SUB>5</SUB>> ]
"18" [label = <(METHOD_RETURN,int)<SUB>4</SUB>> ]
  "7" -> "8" 
  "7" -> "9" 
  "7" -> "10" 
  "7" -> "18" 
  "10" -> "11" 
  "11" -> "12" 
  "12" -> "13" 
  "12" -> "16" 
  "12" -> "17" 
  "13" -> "14" 
  "13" -> "15" 
"""

# 解析AST内容
nodes, edges = parse_ast(ast_content)

# 打印结果
print("Nodes:")
for node_id, label in nodes.items():
    print(f"{node_id}: {label}")

print("\nEdges:")
for source, targets in edges.items():
    for target in targets:
        print(f"{source} -> {target}")
