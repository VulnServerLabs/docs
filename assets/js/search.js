document.addEventListener('DOMContentLoaded', function () {
  const searchInput = document.getElementById('search-box');
  const resultsDiv = document.getElementById('search-results');

  fetch('/docs/search.json')
    .then(response => response.json())
    .then(data => {
      const idx = lunr(function () {
        this.ref('url');
        this.field('title');
        this.field('content');

        data.forEach(doc => this.add(doc));
      });

      searchInput.addEventListener('input', function () {
        const query = this.value.trim();
        resultsDiv.innerHTML = '';

        if (query.length > 1) {
          const results = idx.search(query);
          results.forEach(result => {
            const match = data.find(d => d.url === result.ref);
            const div = document.createElement('div');
            div.innerHTML = `<p><a href="${match.url}">${match.title}</a></p>`;
            resultsDiv.appendChild(div);
          });
        }
      });
    });
});
