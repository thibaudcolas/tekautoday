'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');
var browserify = require('browserify');
var babelify = require('babelify');
var reactify = require('reactify');
var source = require('vinyl-source-stream');
var sass = require('gulp-sass');
var eslint = require('gulp-eslint');
var jscs = require('gulp-jscs');

var reload = browserSync.reload;

gulp.task('build:js', function() {
    return browserify({debug: true})
      .transform([babelify, reactify])
      .require(require.resolve('src/js/main.js'), {entry: true})
      .bundle()
      .pipe(source('bundle.js'))
      .pipe(gulp.dest('src/static/js'))
      .pipe(reload({stream: true}));
});

gulp.task('build:css', function() {
    return gulp.src('src/sass/*.scss')
        .pipe(sass())
        .pipe(gulp.dest('src/static/css'))
        .pipe(reload({stream: true}));
});


gulp.task('lint:js', function() {
    return gulp.src(['src/js/**/*.{js,jsx}'])
        .pipe(eslint())
        .pipe(eslint.format())
        .pipe(jscs());
});

gulp.task('watch', ['build:js', 'build:css'], function() {
    browserSync({
        proxy: 'http://localhost:5000/'
    });

    gulp.watch(['src/*.py', 'src/templates/*.html'], reload);
    gulp.watch(['src/js/**/*.{js,jsx}'], ['build:js']);
    gulp.watch(['src/sass/**/*.{scss,css}'], ['build:css']);
});

gulp.task('default', ['watch']);
