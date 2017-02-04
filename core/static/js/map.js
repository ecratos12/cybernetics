function initMap() {
        var myLatlng = new google.maps.LatLng(50.383540, 30.471088);

        var map = new google.maps.Map(document.getElementById('map'), {
            center: myLatlng,
            scrollwheel: false,
            zoom: 17,
            mapTypeControlOptions: {
                mapTypeIds: [
                    google.maps.MapTypeId.ROADMAP,
                    google.maps.MapTypeId.SATELLITE
                ],
                position: google.maps.ControlPosition.BOTTOM_LEFT
            }
        });

        var widgetDiv = document.getElementById('save-widget');
        map.controls[google.maps.ControlPosition.TOP_LEFT].push(widgetDiv);

        // Append a Save Control to the existing save-widget div.
        var saveWidget = new google.maps.SaveWidget(widgetDiv, {
            place: {
                // ChIJN1t_tDeuEmsRUsoyG83frY4 is the place Id for Google Sydney.
                placeId: 'ChIJN1t_tDeuEmsRUsoyG83frY4',
                location: {lat: -33.866647, lng: 151.195886}
            },
            attribution: {
                source: 'Google Maps JavaScript API',
                webUrl: 'https://developers.google.com/maps/'
            }
        });

        var image = {
            url: 'img/logo-new.png',
            scaledSize: new google.maps.Size(60, 50),
            origin: new google.maps.Point(0,0),
            anchor: new google.maps.Point(0,0)
        };

        var marker = new google.maps.Marker({
            map: map,
            icon: image,
            draggable: true,
            animation: google.maps.Animation.DROP,
            title:"ФАКУЛЬТЕТ КОМП'ЮТЕРНИХ НАУК ТА КІБЕРНЕТИКИ , Глушкова 4Д",
            position: myLatlng
        });
        var contentString = '<div id="content">'+
                '<div id="siteNotice">'+
                '</div>'+
                '<div id="bodyContent">'+
                '<a href="https://www.google.com/maps/dir//50.383071,30.470296/@50.3856054,30.4665489,16z?hl=uk">Украина, Киев, КНУ им. Тараса Шевченка, Факультет кібернетики , Глушкова 4Д</a>'+
                '</div>'+
                '</div>';
        var infowindow = new google.maps.InfoWindow({
            content: contentString
        });
        marker.addListener('click', function() {
            infowindow.open(map, marker, toggleBounce);
        });

    }

    function toggleBounce() {
        if (marker.getAnimation() !== null) {
            marker.setAnimation(null);
        } else {
            marker.setAnimation(google.maps.Animation.BOUNCE);
        }
    }