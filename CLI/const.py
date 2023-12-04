BREADCRUMB_HTML = """
     <li class="home">
                <span property="itemListElement" typeof="ListItem"
                  ><a
                    property="item"
                    typeof="WebPage"
                    title="{{{BREADCRUMB_NAME}}}"
                    href="{{{BREADCRUMB_URL}}}"
                    class="home"
                    ><span property="name">{{{BREADCRUMB_NAME}}}</span></a
                  >
                  <meta property="position" content="1" />
                </span>
              </li>
"""


CATEGORY_HTML = """
    <li
                  class="has-post-thumbnail product type-product post-26933 status-publish first instock product_cat-heat-pump product_cat-heating product_cat-radiators product_tag-heating product_tag-pump product_tag-radiators shipping-taxable purchasable product-type-simple"
                >
                  <div class="lte-item">
                    <div class="lte-image">
                     <a
                        href="{{{PRODUCT_URL}}}"
                        class="woocommerce-LoopProduct-link woocommerce-loop-product__link"
                        ><img
                          width="480"
                          height="560"
                          src="{{{PRODUCT_IMAGE}}}"
                          class="attachment-woocommerce_thumbnail size-woocommerce_thumbnail"
                          alt=""
                          loading="lazy"
                       
                          sizes="(max-width: 480px) 100vw, 480px"
                      /></a>
                    </div>
                    <div class="lte-item-descr">
                      <div
                        class="star-rating"
                        role="img"
                        aria-label="Rated 5.00 out of 5"
                      >
                        <span style="width: 100%"
                          >Rated <strong class="rating">5.00</strong> out of
                          5</span
                        >
                      </div>
                      <a
                        href="{{{PRODUCT_URL}}}
                        class="woocommerce-LoopProduct-link woocommerce-loop-product__link"
                      >
                        <h2 class="woocommerce-loop-product__title">
                          {{{PRODUCT_NAME}}}
                        </h2>
                      </a>
                     
                    
                   
                    </div>
                  </div>
                </li>
"""