// Show loading message while fetching data
function showLoadingMessage(container, message) {
    $(container).html(`<p class="loading-message animate__animated animate__fadeIn">${message}</p>`);
}

// Handle errors gracefully
function showError(container, message) {
    $(container).html(`<p class="error-message animate__animated animate__fadeIn">${message}</p>`);
}

// Handle horizontal scrolling for carousel
function handleCarouselScroll(container, direction) {
    const $carouselContent = $(container);
    const itemWidth = $carouselContent.find('.carousel-item').outerWidth(true); // Include margin in width
    const currentTransform = $carouselContent.css('transform');
    let translateX = 0;

    if (currentTransform !== 'none') {
        translateX = parseFloat(currentTransform.split(',')[4]);
    }

    if (direction === 'left' && translateX < 0) {
        translateX += itemWidth; // Scroll left
    } else if (direction === 'right' && Math.abs(translateX) + $carouselContent.parent().width() < $carouselContent.width()) {
        translateX -= itemWidth; // Scroll right
    }

    $carouselContent.css('transform', `translateX(${translateX}px)`);
}

// Fetch trending crime news using NewsAPI
async function fetchNews(category = '') {
    const apiKey = '87e9b9da28a04c1cba25f4e178c352b9'; // Replace with your actual API key
    const url = `https://newsapi.org/v2/everything?q=crime${category ? `&category=${category}` : ''}&language=en&sortBy=publishedAt&apiKey=${apiKey}`;

    showLoadingMessage('#news-container', 'Loading crime news, please wait...');

    try {
        const response = await $.getJSON(url);
        if (!response.articles || response.articles.length === 0) {
            showError('#news-container', 'No news articles found.');
            return;
        }

        const newsHTML = response.articles.slice(0, 5).map((article, index) => `
            <div class="carousel-item news-article animate__animated animate__fadeIn">
                <a href="#news-detail" class="news-link" data-id="${index}">
                    <img src="${article.urlToImage || 'https://via.placeholder.com/300x200'}" alt="${article.title || 'News Image'}">
                    <h3>${article.title}</h3>
                </a>
                <p>${article.description || 'No description available.'}</p>
            </div>
        `).join('');

        $('#news-container').html(newsHTML);

        // Add click event listeners to news links
        $('.news-link').on('click', function(event) {
            event.preventDefault();
            const id = $(this).data('id');
            showNewsDetail(id);
        });
    } catch (error) {
        console.error('Error fetching news:', error);
        showError('#news-container', 'Failed to load news articles. Please try again later.');
    }
}

// Fetch crime-related podcasts using the Spotify API
async function fetchPodcasts(category = '') {
    const clientId = 'b23eb5b1124342499e78579027dc2092'; // Replace with your actual client ID
    const clientSecret = '1ac7287f719448debaad84f368095edf'; // Replace with your actual client secret

    showLoadingMessage('#podcast-list', 'Loading crime podcasts, please wait...');

    try {
        // Fetch Access Token
        const authResponse = await $.ajax({
            url: 'https://accounts.spotify.com/api/token',
            type: 'POST',
            data: { 'grant_type': 'client_credentials' },
            headers: { 'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret) }
        });

        const token = authResponse.access_token;

        // Use the token to get podcast data
        const podcastResponse = await $.ajax({
            url: `https://api.spotify.com/v1/search?q=crime${category ? ` ${category}` : ''}&type=show&market=IN`,
            type: 'GET',
            headers: { 'Authorization': 'Bearer ' + token }
        });

        if (!podcastResponse.shows.items || podcastResponse.shows.items.length === 0) {
            showError('#podcast-list', 'No podcasts found.');
            return;
        }

        const podcastHTML = podcastResponse.shows.items.map(show => `
            <li class="carousel-item podcast-item animate__animated animate__fadeIn">
                <a href="${show.external_urls.spotify}" target="_blank" aria-label="Listen to ${show.name}">
                    <img src="${show.images[0]?.url || 'https://via.placeholder.com/300x200'}" alt="${show.name}">
                </a>
            </li>
        `).join('');

        $('#podcast-list').html(podcastHTML);
    } catch (error) {
        console.error('Error fetching podcasts:', error);
        showError('#podcast-list', 'Failed to load podcasts. Please try again later.');
    }
}

// Fetch latest investigations using a general crime data API
async function fetchInvestigations(category = '') {
    const apiUrl = `https://crime.getupforchange.com/api/v3/mca?apiKey=test_apikey&cin=U74900TG2016PTC103075`; // Replace with your actual API URL and parameters

    showLoadingMessage('#investigation-container', 'Loading latest investigations, please wait...');

    try {
        const response = await $.getJSON(apiUrl);
        if (!response || response.length === 0) {
            showError('#investigation-container', 'No investigations found.');
            return;
        }

        const investigationsHTML = response.slice(0, 5).map(investigation => `
            <div class="carousel-item investigation-item animate__animated animate__fadeIn">
                <img src="https://via.placeholder.com/300x200" alt="${investigation.category || 'Investigation Image'}">
                <p>${investigation.category}</p>
            </div>
        `).join('');

        $('#investigation-container').html(investigationsHTML);
    } catch (error) {
        console.error('Error fetching investigations:', error);
        showError('#investigation-container', 'Failed to load investigations. Please try again later.');
    }
}

// Initialize the Leaflet map
function initializeMap() {
    const map = L.map('map').setView([51.505, -0.09], 13); // Default coordinates

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Add a marker to the map (example)
    L.marker([51.5, -0.09]).addTo(map)
        .bindPopup('A crime-related location')
        .openPopup();
}

// Initialize floating images with predefined images in HTML
function initializeFloatingImages() {
    const $images = $('.floating-image');
    let currentIndex = 0;

    function changeImage() {
        $images.eq(currentIndex).fadeOut(500, function() {
            currentIndex = (currentIndex + 1) % $images.length;
            $images.eq(currentIndex).fadeIn(500);
        });
    }

    setInterval(changeImage, 3000); // Change image every 3 seconds

    // Initialize with the first image
    $images.first().fadeIn(500);
}

// Fetch crime data and display on dashboard
async function fetchCrimeStats() {
    const url = 'https://api.example.com/crime-stats'; // Replace with your actual API URL

    showLoadingMessage('#crime-stats', 'Loading crime statistics, please wait...');

    try {
        const response = await $.getJSON(url);
        if (!response || response.length === 0) {
            showError('#crime-stats', 'No crime statistics found.');
            return;
        }

        const statsHTML = response.map(stat => `
            <div class="stat-item">
                <h3>${stat.type}</h3>
                <p>${stat.count} cases</p>
            </div>
        `).join('');

        $('#crime-stats').html(statsHTML);
    } catch (error) {
        console.error('Error fetching crime stats:', error);
        showError('#crime-stats', 'Failed to load crime statistics. Please try again later.');
    }
}

// Display detailed news content
function showNewsDetail(id) {
    // You could use a modal or a dedicated section to display the detailed news
    const $newsContainer = $('#news-detail');
    
    // Fetch news details from the local data
    const article = $('#news-container .news-link').eq(id).closest('.carousel-item');
    const title = article.find('h3').text();
    const description = article.find('p').text();
    const imageUrl = article.find('img').attr('src');

    // Display news details (could be a modal or a new section)
    $newsContainer.html(`
        <h2>${title}</h2>
        <img src="${imageUrl}" alt="${title}">
        <p>${description}</p>
        <button onclick="window.history.back()">Back to News</button>
    `).show();

    // Optionally, scroll to the news detail section
    $('html, body').animate({
        scrollTop: $newsContainer.offset().top
    }, 500);
}

// Event Listeners for Carousel Navigation
$('.arrow-btn.news-left').on('click', () => handleCarouselScroll('.news-carousel .carousel-content', 'left'));
$('.arrow-btn.news-right').on('click', () => handleCarouselScroll('.news-carousel .carousel-content', 'right'));
$('.arrow-btn.investigation-left').on('click', () => handleCarouselScroll('.investigation-carousel .carousel-content', 'left'));
$('.arrow-btn.investigation-right').on('click', () => handleCarouselScroll('.investigation-carousel .carousel-content', 'right'));

// Document Ready
$(document).ready(function() {
    fetchNews();
    fetchPodcasts();
    fetchInvestigations();
    fetchCrimeStats();
    initializeMap();
    initializeFloatingImages();
});

const heroSection = document.querySelector('.hero-section');

const images = [
    'https://images.unsplash.com/photo-1718592168437-8382e5b97736?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGNyaW1lfGVufDB8fDB8fHww',
    'https://images.unsplash.com/photo-1571134441329-4baf7f43a3d1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTU5fHxjcmltZXxlbnwwfHwwfHx8MA%3D%3D',
    'https://images.unsplash.com/photo-1605806616949-1e87b487fc2f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3JpbWV8ZW58MHx8MHx8fDA%3D',
    'https://images.unsplash.com/photo-1704971175047-03466f0ce02f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NjB8fGNyaW1lfGVufDB8fDB8fHww',
    'https://images.unsplash.com/photo-1595157215485-b2fc4d90a731?w=500&auto=format&fit=crop&q=60'
];

let currentIndex = 0;

function changeBackgroundImage() {
    currentIndex = (currentIndex + 1) % images.length;
    heroSection.style.backgroundImage = `linear-gradient(135deg, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('${images[currentIndex]}')`;
}

// Change image every 5 seconds
setInterval(changeBackgroundImage, 5000);

