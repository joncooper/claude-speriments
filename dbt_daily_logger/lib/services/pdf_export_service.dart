import 'dart:io';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets' as pw;
import 'package:printing/printing.dart';
import 'package:share_plus/share_plus.dart';
import 'package:path_provider/path_provider.dart';
import 'package:intl/intl.dart';
import '../models/diary_entry.dart';

class PDFExportService {
  Future<void> exportEntriesToPDF(List<DiaryEntry> entries) async {
    final pdf = pw.Document();

    // Add cover page
    pdf.addPage(
      pw.Page(
        pageFormat: PdfPageFormat.a4,
        build: (context) => pw.Column(
          crossAxisAlignment: pw.CrossAxisAlignment.start,
          children: [
            pw.Text(
              'DBT Daily Logger',
              style: pw.TextStyle(
                fontSize: 32,
                fontWeight: pw.FontWeight.bold,
              ),
            ),
            pw.SizedBox(height: 16),
            pw.Text(
              'Diary Card Export',
              style: const pw.TextStyle(fontSize: 24),
            ),
            pw.SizedBox(height: 8),
            pw.Text(
              'Generated: ${DateFormat('MMMM d, y').format(DateTime.now())}',
              style: pw.TextStyle(
                fontSize: 14,
                color: PdfColors.grey700,
              ),
            ),
            pw.SizedBox(height: 8),
            pw.Text(
              'Total Entries: ${entries.length}',
              style: pw.TextStyle(
                fontSize: 14,
                color: PdfColors.grey700,
              ),
            ),
          ],
        ),
      ),
    );

    // Add entry pages
    for (var entry in entries) {
      pdf.addPage(
        pw.Page(
          pageFormat: PdfPageFormat.a4,
          build: (context) => _buildEntryPage(entry),
        ),
      );
    }

    // Save and share
    await _savePDF(pdf);
  }

  Future<void> exportSingleEntry(DiaryEntry entry) async {
    final pdf = pw.Document();

    pdf.addPage(
      pw.Page(
        pageFormat: PdfPageFormat.a4,
        build: (context) => _buildEntryPage(entry),
      ),
    );

    await _savePDF(pdf);
  }

  pw.Widget _buildEntryPage(DiaryEntry entry) {
    return pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: [
        // Date header
        pw.Container(
          padding: const pw.EdgeInsets.all(16),
          decoration: pw.BoxDecoration(
            color: PdfColors.teal,
            borderRadius: pw.BorderRadius.circular(8),
          ),
          child: pw.Row(
            children: [
              pw.Expanded(
                child: pw.Text(
                  DateFormat('EEEE, MMMM d, y').format(entry.date),
                  style: pw.TextStyle(
                    fontSize: 18,
                    fontWeight: pw.FontWeight.bold,
                    color: PdfColors.white,
                  ),
                ),
              ),
            ],
          ),
        ),
        pw.SizedBox(height: 16),

        // Daily basics
        if (entry.sleepHours != null || entry.tookMedication != null) ...[
          _buildSection(
            'Daily Basics',
            [
              if (entry.sleepHours != null)
                'Sleep: ${entry.sleepHours} hours',
              if (entry.tookMedication != null)
                'Medication: ${entry.tookMedication! ? "Taken" : "Not taken"}',
            ],
          ),
          pw.SizedBox(height: 12),
        ],

        // Emotions
        if (entry.emotions.isNotEmpty) ...[
          _buildSection(
            'Emotions',
            entry.emotions.entries
                .map((e) => '${e.key}: ${e.value}/10')
                .toList(),
          ),
          pw.SizedBox(height: 12),
        ],

        // Urges
        if (entry.urges.isNotEmpty) ...[
          _buildSection(
            'Urges',
            entry.urges.entries.map((e) => '${e.key}: ${e.value}/10').toList(),
          ),
          pw.SizedBox(height: 12),
        ],

        // Target behaviors
        if (entry.targetBehaviors.isNotEmpty) ...[
          _buildSection(
            'Target Behaviors',
            entry.targetBehaviors,
          ),
          pw.SizedBox(height: 12),
        ],

        // Skills used
        if (entry.skillsUsed.isNotEmpty) ...[
          _buildSection(
            'DBT Skills Used',
            entry.skillsUsed,
          ),
          pw.SizedBox(height: 12),
        ],

        // Notes
        if (entry.notes.isNotEmpty) ...[
          _buildSection(
            'Notes',
            [entry.notes],
          ),
        ],
      ],
    );
  }

  pw.Widget _buildSection(String title, List<String> items) {
    return pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: [
        pw.Text(
          title,
          style: pw.TextStyle(
            fontSize: 16,
            fontWeight: pw.FontWeight.bold,
          ),
        ),
        pw.SizedBox(height: 8),
        pw.Container(
          padding: const pw.EdgeInsets.all(12),
          decoration: pw.BoxDecoration(
            color: PdfColors.grey100,
            borderRadius: pw.BorderRadius.circular(8),
          ),
          child: pw.Column(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: items
                .map((item) => pw.Padding(
                      padding: const pw.EdgeInsets.only(bottom: 4),
                      child: pw.Text(
                        '• $item',
                        style: const pw.TextStyle(fontSize: 12),
                      ),
                    ))
                .toList(),
          ),
        ),
      ],
    );
  }

  Future<void> _savePDF(pw.Document pdf) async {
    try {
      // Save to temporary directory
      final tempDir = await getTemporaryDirectory();
      final timestamp = DateFormat('yyyyMMdd_HHmmss').format(DateTime.now());
      final file = File('${tempDir.path}/dbt_diary_$timestamp.pdf');
      await file.writeAsBytes(await pdf.save());

      // Share the file
      await Share.shareXFiles(
        [XFile(file.path)],
        subject: 'DBT Diary Card Export',
      );
    } catch (e) {
      print('Error saving PDF: $e');
      rethrow;
    }
  }

  Future<void> printEntry(DiaryEntry entry) async {
    final pdf = pw.Document();

    pdf.addPage(
      pw.Page(
        pageFormat: PdfPageFormat.a4,
        build: (context) => _buildEntryPage(entry),
      ),
    );

    await Printing.layoutPdf(
      onLayout: (PdfPageFormat format) async => pdf.save(),
    );
  }
}
