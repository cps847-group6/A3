'use strict';

var mainApp = angular.module('mainApp', ["ngRoute"]);

mainApp.factory('currWeather', function($http) {
    return { 
      getweather: function() {
        var weather = { temp: {}, clouds: null };
        $http.jsonp('http://api.openweathermap.org/data/2.5/weather?q=Toronto,at&units=metric&callback=JSON_CALLBACK&APPID=497351da5f903f448e30711b83cab855').success(function(data) {
            if (data) {
                if (data.main) {
                    weather.temp.current = data.main.temp;
                }
                weather.clouds = data.clouds ? data.clouds.all : undefined;
            }
        });
        return weather;
      }
    }; 
});

mainApp.filter('temp', function($filter) {
    return function(input, decimal) {
        var numberFilter = $filter('number');
        return numberFilter(input, decimal) + '\u00B0C';
    };
});

mainApp.controller('WeatherCtrl', function ($scope, currWeather) {
    $scope.date = new Date();
	$scope.weather = currWeather.getweather();
});


mainApp.config(function($routeProvider) {
    $routeProvider
	.when("/", {
        template : "<h1> Welcome to MyCompany Inc.! </h1>"
	})
    .when("/about", {
        template : "<h1>About Us</h1><p>MyCompany Inc. is an IT consulting company in the heart of downtown Toronto. Our focus is to provide the best cost-efficient solutions for our clients.<p/>"
    })
    .when("/service", {
        template : "<h1>Our Services</h1><p>Our services include: RMM, IROD, Online Backup and Restore, Hosted Solutions, Laptop Data Encryption, and Asset Management.</p>"
    })
    .when("/customer", {
        template : "<h1>Our Customers</h1><p>Our clients include: Chair-man Mills, Knightsbridge, Queenston, and Quark Expeditions.</p>"
    });
});


