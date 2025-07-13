const search = document.getElementById('search');
const results = document.getElementById('results');

search.addEventListener('input', () => {
    const query = search.value.toLowerCase();
    results.innerHTML = '';

    Object.keys(dict).forEach(word => {
    if (word.toLowerCase().includes(query)) {
        const li = document.createElement('li');
        const filename = word.replace(/[^a-z0-9]/gi, '_') + '.html';
        li.innerHTML = `<a href="words/${filename}">${word}</a>`;
        results.appendChild(li);
    }
    });
});