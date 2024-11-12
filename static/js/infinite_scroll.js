let page = 1;

window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 500) {
        loadMorePosts();
    }
});

function loadMorePosts() {
    page += 1;
    fetch(`/load-more-posts/?page=${page}`)
        .then(response => response.text())
        .then(data => {
            document.querySelector('.posts-container').insertAdjacentHTML('beforeend', data);
        })
        .catch(error => console.log('Erreur de chargement :', error));
}
