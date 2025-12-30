const API_BASE = "/api/recipes";
let currentPage = 1;
let currentLimit = 15;
let totalPages = 1;
let currentFilters = {};
let allRecipes = [];

// --- Helper Functions ---

// Generate star rating HTML (Corrected Logic)
function generateStars(rating) {
    const numericRating = parseFloat(rating) || 0;
    let starsHtml = '';
    
    // Determine the number of full stars
    const fullStars = Math.floor(numericRating);
    // Determine if a half star is needed (e.g., for 4.5)
    const halfStar = numericRating % 1 >= 0.5 ? 1 : 0;
    // Calculate remaining empty stars
    const emptyStars = 5 - fullStars - halfStar;
    
    // Build the string: all full stars, then a potential half star, then empty stars
    starsHtml += '★'.repeat(fullStars);
    
    if (halfStar) {
        // If you had a specific half-star character, you'd use it here.
        // Since you only have full/empty, a 4.5 will look like 4 full, 1 empty.
        // For a rating of exactly 5.0, halfStar will be 0, and emptyStars will be 0.
    }

    starsHtml += '☆'.repeat(emptyStars);
    
    return starsHtml;
}


// Cleans filters by removing empty strings/nulls
function cleanFilters(filters) {
    return Object.fromEntries(
        Object.entries(filters).filter(([_, value]) => value !== '' && value !== null && value !== undefined)
    );
}

// --- Fetching Data ---

// Fetch recipes (paginated or searched)
async function fetchRecipes(page = 1, limit = 15, filters = {}) {
    currentPage = page;
    currentLimit = limit;
    currentFilters = filters;

    const activeFilters = cleanFilters(filters);
    const isSearch = Object.keys(activeFilters).length > 0;
    
    // Build parameters, including page/limit
    const params = new URLSearchParams({ page, limit, ...activeFilters });
    
    // Select endpoint based on whether filters are active
    const url = isSearch ? `${API_BASE}/search?${params}` : `${API_BASE}?${params}`;
    
    try {
        const response = await fetch(url);
        const data = await response.json();
        
        // Check if the backend response structure is valid
        if (data && data.data) {
            allRecipes = data.data;
            
            // The /search endpoint may not return 'total', so we handle both cases
            if (data.total !== undefined) {
                 totalPages = Math.ceil(data.total / limit);
            } else if (isSearch) {
                // If in search mode and total is missing, assume we're just loading one page
                totalPages = page; 
            }

            renderTable(allRecipes);
            renderPagination(page, totalPages);
            document.getElementById('no-data').style.display = allRecipes.length === 0 ? 'block' : 'none';
            document.getElementById('no-results').style.display = 'none';
        } else {
            document.getElementById('no-results').style.display = 'block';
            document.getElementById('no-data').style.display = 'none';
        }
    } catch (error) {
        console.error('Error fetching recipes:', error);
        document.getElementById('no-results').style.display = 'block';
        document.getElementById('no-data').style.display = 'none';
    }
}

// --- Rendering Data ---

// Render table
function renderTable(recipes) {
    const tbody = document.getElementById('table-body');
    tbody.innerHTML = '';
    recipes.forEach(recipe => {
        const row = document.createElement('tr');
        row.onclick = () => openDrawer(recipe);
        
        const titleCell = document.createElement('td');
        titleCell.textContent = recipe.title ? (recipe.title.length > 30 ? recipe.title.substring(0, 30) + '...' : recipe.title) : 'N/A';
        titleCell.title = recipe.title; // Tooltip for full title
        
        const cuisineCell = document.createElement('td');
        cuisineCell.textContent = recipe.cuisine || 'N/A';
        
        const ratingCell = document.createElement('td');
        ratingCell.innerHTML = generateStars(recipe.rating || 0);
        
        const totalTimeCell = document.createElement('td');
        totalTimeCell.textContent = recipe.total_time || 'N/A';
        
        const servesCell = document.createElement('td');
        servesCell.textContent = recipe.serves || 'N/A';
        
        row.appendChild(titleCell);
        row.appendChild(cuisineCell);
        row.appendChild(ratingCell);
        row.appendChild(totalTimeCell);
        row.appendChild(servesCell);
        tbody.appendChild(row);
    });
}

// Render pagination
function renderPagination(page, totalPages) {
    document.getElementById('page-info').textContent = `Page ${page} of ${totalPages}`;
    document.getElementById('prev-btn').disabled = page === 1;
    document.getElementById('next-btn').disabled = page >= totalPages;
}

// Open drawer with details
function openDrawer(recipe) {
    document.getElementById('drawer-title').textContent = `${recipe.title || 'N/A'} - ${recipe.cuisine || 'N/A'}`;
    document.getElementById('drawer-description').textContent = `Description: ${recipe.description || 'N/A'}`;
    document.getElementById('total-time-value').textContent = recipe.total_time || 'N/A';
    document.getElementById('cook-time-value').textContent = recipe.cook_time || 'N/A';
    document.getElementById('prep-time-value').textContent = recipe.prep_time || 'N/A';
    
    const nutritionTbody = document.getElementById('nutrition-table').querySelector('tbody');
    nutritionTbody.innerHTML = '';
    if (recipe.nutrients) {
        Object.entries(recipe.nutrients).forEach(([key, value]) => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${key}</td><td>${value}</td>`;
            nutritionTbody.appendChild(row);
        });
    }
    
    document.getElementById('drawer').classList.add('open');
}

// Event listeners (Using addEventListener for modern practice)
document.getElementById('search-btn').addEventListener('click', () => {
    currentFilters = {
        calories: document.getElementById('calories').value,
        title: document.getElementById('title').value,
        cuisine: document.getElementById('cuisine').value,
        total_time: document.getElementById('total_time').value,
        rating: document.getElementById('rating').value,
    };
    currentPage = 1;
    fetchRecipes(currentPage, currentLimit, currentFilters);
});

document.getElementById('clear-btn').addEventListener('click', () => {
    document.querySelectorAll('#filters input').forEach(input => input.value = '');
    currentFilters = {};
    currentPage = 1;
    fetchRecipes(currentPage, currentLimit);
});

document.getElementById('prev-btn').addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        fetchRecipes(currentPage, currentLimit, currentFilters);
    }
});

document.getElementById('next-btn').addEventListener('click', () => {
    if (currentPage < totalPages) {
        currentPage++;
        fetchRecipes(currentPage, currentLimit, currentFilters);
    }
});

document.getElementById('limit-select').addEventListener('change', (e) => {
    currentLimit = parseInt(e.target.value);
    currentPage = 1;
    fetchRecipes(currentPage, currentLimit, currentFilters);
});

document.getElementById('close-drawer').addEventListener('click', () => {
    document.getElementById('drawer').classList.remove('open');
});

// Initial load
fetchRecipes();
