var requestapp = angular.module('requestapp',[]);

requestapp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

requestapp.controller('ListCategory', function ListCategory($scope, $log, $http){
    $scope.items = {}

    $scope.loadItems = function(){
        $scope.items = $http.get('/category-list-rest/').then(function(response){
            $scope.page = response.data;
        });
    };

    $scope.filter = function(){

        var data = $.param({
                search: $scope.search,
                page:1});

            var config = {
                headers : {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
                }
            }

        $http.post('/category-list-rest/', data,config)
        .success(function (data, status, headers, config) {
            $scope.page = data;
        })
        .error(function (data, status, header, config) {

        });
    };
});