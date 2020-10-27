$(document).ready(function () {
    let radiant_pool = []
    let dire_pool = []

    $(".hero-select-left").click(function () {
        let hero_id = $(this).data("heroid");
        add_to_pool(radiant_pool, hero_id)
    })

    $(".hero-select-right").click(function () {
        let hero_id = $(this).data("heroid");
        add_to_pool(dire_pool, hero_id)
    })

});

function add_to_pool(pool, id) {
    if (!pool.includes(id) && pool.length < 6) {
        pool.push(id)
    }
    console.log(pool)
}

/**
 * 
 * @param {object} pool 
 * @param {int} id 
 */
function remove_from_pool(pool, id) {
    if (pool >= 0) {
        let idx = pool.indexOf(id)
        if (idx > -1) {
            array.splice(idx, 1);
        }
    }
}