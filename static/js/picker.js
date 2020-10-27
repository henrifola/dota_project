$(document).ready(function () {
    let radiant_pool = []
    let dire_pool = []

    $(".hero-select-left").click(function () {
        let hero_id = $(this).data("heroid");
        add_to_pool(radiant_pool, hero_id)
        update_images("radiant", radiant_pool)
        console.log("radiant: " + radiant_pool + "\ndire: " + dire_pool)

    })

    $(".hero-select-right").click(function () {
        let hero_id = $(this).data("heroid");
        add_to_pool(dire_pool, hero_id)
        update_images("dire", dire_pool)
        console.log("radiant: " + radiant_pool + "\ndire: " + dire_pool)
    })

    $(".hero-pool-radiant").click(function () {
        let hero_id = $(this).data("heroid");
        if (hero_id !== -1) {
            $(this).data("heroid", -1);
            remove_from_pool(radiant_pool, hero_id)
            refresh_images()
            update_images("radiant", radiant_pool)
            update_images("dire", dire_pool)

            console.log("radiant: " + radiant_pool + "\ndire: " + dire_pool)
        }
    })

    $(".hero-pool-dire").click(function () {
        let hero_id = $(this).data("heroid");
        if (hero_id !== -1) {
            $(this).data("heroid", -1);
            remove_from_pool(dire_pool, hero_id)
            refresh_images()
            update_images("dire", dire_pool)
            update_images("radiant", radiant_pool)

            console.log("radiant: " + radiant_pool + "\ndire: " + dire_pool)

        }
    })
});

function refresh_images(){
    $(".hero-pool").each(function () {
        $(this).attr("src", "/static/img/placeholder.png")
    })
}

function update_images(faction, pool) {
    let imgs = $(`.hero-pool-${faction}`)
    
    for (const [i, hero_id] of pool.entries()) {
        $(imgs[i]).attr("src", `/static/img/avatar-sb/${hero_id.toString()}.png`)
        $(imgs[i]).css("height", "60px")
        $(imgs[i]).data("heroid", hero_id)
    }

}

function add_to_pool(pool, id) {
    if (!pool.includes(id) && pool.length < 5) {
        pool.push(id)
    }
}

function remove_from_pool(pool, id) {
    if (pool.length >= 0) {
        let idx = pool.indexOf(id)
        if (idx > -1) {
            pool.splice(idx, 1);
        }
    }
}