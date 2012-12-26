'use strict';

/* Controllers */

function MyCtrl1() {}
MyCtrl1.$inject = [];


function MyCtrl2() {
}
MyCtrl2.$inject = [];


function CreateCampCtrl($scope,$http){
	$scope.save = function() {
    	$http.put('/save.py', $scope.Campaign);
  	};
	$http.get('campaigns').success(function(data) {
		$scope.campaigns = data;
		angular.extend($scope.version3campaign.data, data);
	});
	$http.get('types').success(function(data) {
		$scope.types = data;
		angular.extend($scope.version3type.data, data);
	});
	
	$scope.orderProp = 'fields.type';
	
	$http.get('products').success(function(data) {
		$scope.products = data;
		angular.extend($scope.version3product.data, data);
	});	
	$http.get('channels').success(function(data) {
		$scope.channels = data;
		angular.extend($scope.version3channel.data, data);
	});	
	$http.get('reps').success(function(data) {
		$scope.reps = data;
		angular.extend($scope.version3rep.data, data);
	});	
	$http.get('CPs').success(function(data) {
		$scope.CPs = data;
		angular.extend($scope.version3CP.data, data);
	});	
	$scope.version3type = {
    	data: []
  	};	
	$scope.version3campaign = {
    	data: []
  	};		
  	$scope.version3product = {
    	data: []
  	};	
	$scope.version3channel = {
    	data: []
  	};		
  	$scope.version3rep = {
    	data: []
  	};	
	$scope.version3CP = {
    	data: []
  	};		
  	
}


function CampListCtrl($scope, $http){ /*, $location) { */
	$http.get('campaigns').success(function(data) {
		$scope.campaigns = data;
	});
	$scope.orderProp = 'fields.campaign';
/*	$scope.createCampaign = function(){
		$location.path('create'); 
		$scope.apply(); 
   } */
 }
 
function CampActualCtrl($scope, $routeParams, $http){
	$http.get('campaigns/' + $routeParams.campaignId).success(function(data) {
    	$scope.actuals = data;
  	});
  	$scope.orderProp = 'fields.date';
 	$scope.campaignId = $routeParams.campaignId;
 	$scope.hello = function(name) {
      alert('Hello ' + (name || 'world') + '!');
  };
}


/*
function RepListCtrl($scope, $http) {
	$http.get('/media/javascript/rep.json').success(function(data) {
		$scope.reps = data;
	});
	$scope.orderProp = 'pk';
 }
 
RepListCtrl.$inject = ['$scope', '$http'];
*/

/*
var myApp = angular.module('myApp', [], function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
*/
/*
function RepListCtrl($scope) {
  $scope.reps = [ 
	{"pk": 42, "model": "finance.rep", 
	"fields": {"first_name": "Lauren", "last_name": "Gates", "employeeID": "215", "manager": 5, "date_of_hire": "2011-05-31", "repID": "LG", "department": 1, "channel": 3}}, 
	{"pk": 73, "model": "finance.rep", 
	"fields": {"first_name": "Lindsay E.", "last_name": "Glancz", "employeeID": "350", "manager": 8, "date_of_hire": "2012-05-29", "repID": "LIG", "department": 1, "channel": 3}}, 
	{"pk": 10, "model": "finance.rep", "fields": {"first_name": "Nicholas", "last_name": "Guerriero", "employeeID": "84", "manager": null, "date_of_hire": "2009-05-11", "repID": "NG", "department": 2, "channel": 1}},
  ];
  
  $scope.orderProp = 'date_of_hire';
  
} 
*/

 