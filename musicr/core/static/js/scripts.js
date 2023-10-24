<script>
    // Adicione um evento de clique aos botões de expansão
    const albumToggles = document.querySelectorAll('.album-toggle');
    albumToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const albumDetails = toggle.nextElementSibling;
            albumDetails.style.display = albumDetails.style.display === 'block' ? 'none' : 'block';
        });
    });
</script>