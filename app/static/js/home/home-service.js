'use strict';

angular.module('myapp').factory('SnapshotServices', ['$http', '$resource', function ($http, $resource) {
    var srv = {};

    srv.getSnapshots = function () {
        return $http({
            url: '/api/db/snapshots',
            dataType: "json",
            method: "GET"
        }).then(function (res) {
            return res.data;
        });
    };

    srv.backupDatabase = function (callback) {
        return $http({
            url: '/api/db/backup',
            dataType: "json",
            method: "POST"
        }).then(function (res) {
            if (typeof(callback) == "function") {
                callback();
            }
            return res.data;
        });
    };

    srv.restoreDatabase = function (snapshotId, callback) {
        return $http({
            url: '/api/db/restore',
            dataType: "json",
            method: "POST",
            data: {
                snapshotId: snapshotId
            }
        }).then(function (res) {
            if (typeof(callback) == "function") {
                callback();
            }
            return res.data;
        });
    };

    return srv;
}]);
