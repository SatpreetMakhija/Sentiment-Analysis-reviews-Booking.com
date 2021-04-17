mapboxgl.accessToken = 'pk.eyJ1IjoiamVlbmIiLCJhIjoiY2tuajFrM2VhMjV0OTJxb2FuMWs4OTF3NCJ9.poNlFPLHkm4oKPCo6XI1Aw';

const hotelsData = require("./data/polarity/bangkok.json"); //with path


const map = new mapboxgl.Map({
	container: 'map', // container ID
	style: 'mapbox://styles/mapbox/streets-v11', // style URL
	center: [0, 40], // starting position [lng, lat]
	zoom: 0 // starting zoom
});


const nav = new mapboxgl.NavigationControl()
	map.addControl(nav)
;

var direction = new MapboxDirections({
	accessToken: mapboxgl.accessToken
});

map.addControl(direction,'top-left')
;


var geojson = {
	type: 'FeatureCollection',
	features: [{
	  type: 'Feature',
	  geometry: {
		type: 'Point',
		coordinates: [-77.032, 38.913]
	  },
	  properties: {
		title: 'Mapbox',
		description: 'Washington, D.C.'
	  }
	},
	{
	  type: 'Feature',
	  geometry: {
		type: 'Point',
		coordinates: [-122.414, 37.776]
	  },
	  properties: {
		title: 'Mapbox',
		description: 'San Francisco, California'
	  }
	}]
};


// add markers to map
	geojson.features.forEach(function (marker) {
	// create a DOM element for the marker
	var el = document.createElement('div');
	el.className = 'marker';
	
	
	 
	// el.addEventListener('click', function () {
	// window.alert(marker.properties.message);
	// });
	 
	// add marker to map
	new mapboxgl.Marker(el)
  	.setLngLat(marker.geometry.coordinates)
  	.setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
    .setHTML('<h3>' + marker.properties.title + '</h3><p>' + marker.properties.description + '</p>'))
  	.addTo(map);
	});
