'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');
var browserify = require('browserify');
var babelify = require('babelify');
var reactify = require('reactify');
var source = require('vinyl-source-stream');

var reload = browserSync.reload;

gulp.task('build', function() {
    return browserify({debug: true})
      .transform([babelify, reactify])
      .require(require.resolve('./src/js/main.js'), {entry: true})
      .bundle()
      .pipe(source('bundle.js'))
      .pipe(gulp.dest('./src/static/js'))
      .pipe(reload({stream: true}));
});

gulp.task('watch', ['build'], function() {
    browserSync({
        proxy: 'http://localhost:5000/'
    });

    gulp.watch(['src/js/**/*.{js,jsx}'], ['build']);
});

gulp.task('default', ['watch']);
