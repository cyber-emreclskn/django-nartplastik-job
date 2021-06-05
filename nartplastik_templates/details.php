<?php include "TEMPLATE.php"; ?>

<div class="details">
    <div class="container">
        <div class="row">
            <div class="col-md-6 col-12">
                <div class="gallery">
                    <div class="gallery-item">
                        <input type="radio" id="img-1" checked name="gallery" class="gallery-selector"/>
                        <img class="gallery-img" src="https://picsum.photos/id/1015/600/400.jpg" alt=""/>
                        <label for="img-1" class="gallery-thumb"><img src="https://picsum.photos/id/1015/150/100.jpg" alt=""/></label>
                    </div>
                    <div class="gallery-item">
                        <input type="radio" id="img-2" name="gallery" class="gallery-selector"/>
                        <img class="gallery-img" src="https://picsum.photos/id/1039/600/400.jpg" alt=""/>
                        <label for="img-2" class="gallery-thumb"><img src="https://picsum.photos/id/1039/150/100.jpg" alt=""/></label>
                    </div>
                    <div class="gallery-item">
                        <input type="radio" id="img-3" name="gallery" class="gallery-selector"/>
                        <img class="gallery-img" src="https://picsum.photos/id/1057/600/400.jpg" alt=""/>
                        <label for="img-3" class="gallery-thumb"><img src="https://picsum.photos/id/1057/150/100.jpg" alt=""/></label>
                    </div>
                    <div class="gallery-item">
                        <input type="radio" id="img-4" name="gallery" class="gallery-selector"/>
                        <img class="gallery-img" src="https://picsum.photos/id/106/600/400.jpg" alt=""/>
                        <label for="img-4" class="gallery-thumb"><img src="https://picsum.photos/id/106/150/100.jpg" alt=""/></label>
                    </div>
                </div>
            </div>
            <div class="col-md-6 col-12">
                <div class="product-exp">
                    <h1 class="title">Ürünün adı olacak yazı</h1>
                    <p><b class="bold cat">Ürün kategorisi:</b> Kategori Adı</p>
                    <p>
                        <b class="bold exp">Ürün Açıklaması:</b>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam consectetur delectus dignissimos distinctio eos error eum, harum ipsam ipsum mollitia necessitatibus nesciunt officiis omnis repellat, saepe voluptatem voluptatum. Deleniti, quidem!
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam consectetur delectus dignissimos distinctio eos error eum, harum ipsam ipsum mollitia necessitatibus nesciunt officiis omnis repellat, saepe voluptatem voluptatum. Deleniti, quidem!
                    </p>
                </div>
                <div class="btn" data-aos="zoom-in">
                    <a href="products.php" class="btn-hover color">Tüm Benzer Ürünleri Gör</a>
                </div>
            </div>
        </div>
    </div>
    <div class="products">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="section mt-4">
                        <div class="head">
                            <h1 data-value="Benzer Ürünler?">Benzer Ürünler?</h1>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-3 col-sm-6 col-12" data-aos="zoom-in">
                    <div class="product-card">
                        <a href="details.php">
                            <img src="http://localhost/HtmlExamples/images/4.jpg" alt="yüklenemedi..">
                            <h3>Ürün adı olacak yazı</h3>
                            <p>Kategori Adı</p>
                        </a>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6 col-12" data-aos="zoom-in">
                    <div class="product-card">
                        <a href="details.php">
                            <img src="http://localhost/HtmlExamples/images/4.jpg" alt="yüklenemedi..">
                            <h3>Ürün adı olacak yazı</h3>
                            <p>Kategori Adı</p>
                        </a>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6 col-12" data-aos="zoom-in">
                    <div class="product-card">
                        <a href="details.php">
                            <img src="http://localhost/HtmlExamples/images/4.jpg" alt="yüklenemedi..">
                            <h3>Ürün adı olacak yazı</h3>
                            <p>Kategori Adı</p>
                        </a>
                    </div>
                </div>
                <div class="col-md-3 col-sm-6 col-12" data-aos="zoom-in">
                    <div class="product-card">
                        <a href="details.php">
                            <img src="http://localhost/HtmlExamples/images/4.jpg" alt="yüklenemedi..">
                            <h3>Ürün adı olacak yazı</h3>
                            <p>Kategori Adı</p>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<?php include "TEMPLATE_FOOTER.php"; ?>
