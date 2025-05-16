import os
import json
import frontmatter

def collect_docs(base_path):
    pages = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                    title = post.get('title', os.path.splitext(file)[0])
                    content = post.content.replace('\n', ' ')
                    url = path.replace(base_path, '/docs').replace('index.md', '').replace('.md', '.html')
                    pages.append({
                        "url": url,
                        "title": title,
                        "content": content[:1000]  # limit content to first 1000 chars
                    })
    return pages

if __name__ == "__main__":
    base = "."
    output_file = os.path.join(base, "search.json")
    data = collect_docs(base)
    with open(output_file, "w", encoding='utf-8') as out:
        json.dump(data, out, indent=2)
    print(f"✅ search.json generated with {len(data)} entries.")
