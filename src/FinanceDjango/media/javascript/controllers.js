'use strict';

/* Controllers */

function MyCtrl1() {}
MyCtrl1.$inject = [];


function MyCtrl2() {
}
MyCtrl2.$inject = [];




function CampListCtrl($scope, $http) {
	$http.get('/media/javascript/campaign.json').success(function(data) {
		$scope.campaigns = data;
	});
	$scope.orderProp = 'fields.campaign';
 }
 
function CampActualCtrl($scope, $routeParams, $http){
	$http.get('/media/json/actual' + $routeParams.campaignId + '.json').success(function(data) {
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

 