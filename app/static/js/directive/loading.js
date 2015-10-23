/**
 * Created by Tran Huu Cuong on 2015-10-23 15:53:00.
 */
/*global todomvc, angular */
'use strict';

/**
 * useful to take a photo from native camera
 */
angular.module('myapp').directive('loading', [
    function () {
        function init(scope, element, attrs) {
            scope.showLoading = function () {
                $('#loading').show();
            };
            scope.hideLoading = function () {
                $('#loading').hide()
            };
        }

        var template = '<div class="loading-container" id="loading">'
            + '<div class="loading-content">'
            + '<div class="sk-folding-cube">'
            + '<div class="sk-cube1 sk-cube"></div>'
            + '<div class="sk-cube2 sk-cube"></div>'
            + '<div class="sk-cube4 sk-cube"></div>'
            + '<div class="sk-cube3 sk-cube"></div>'
            + '</div></div></div>';
        return {
            restrict: 'ACE',
            template: template,
            link: init
        };
    }]);
